##基本功能
1、pageobject分层时,page的组织和层级  
2、元素定位:通过父节点找子节点、通过子节点确定父节点、找兄弟节点  
3、多设备分配测试任务运行  
4、断言相关  
5、日志和报告  
6、业务复用和维护  

## 需要安装的
```brew install allure-commandline``` （生成allure报告的工具）  

安装requment.txt里面的第三方包

```
selenium
Appium-Python-Client
pytest
allure-pytest
```
## 常用命令
```
adb devices
adb kill-server
adb shell "dumpsys window w | grep name="  (获取当前页面的Activity)
```
运行appium服务器（带有日志形式,no-reset形式,多设备时指定连接设备）

```appium --address 0.0.0.0 --port 4723 --log "appium.log" --log-timestamp --local-timezone  --no-reset  --session-override  -U 192.168.56.101:5555```

# 快速使用
### 检测环境：
在apk中添加要测的app包  
运行env_check.py检测环境  

### 原理讲解
**0：分层概念**  
page集、page类、page类加载方法（load_android、load_ios）、page元素、元素的属性  
**1、配置文件**  
路径: 项目/config/config_android.py  
需要修改的有：app包路径、appium版本号、devices相关、报告相关路径  
**2、编写pages**   
 路径： 项目/pages  
**创建一个page集合**，在pageset.py中创建page集合类然后添加类属性page类（page类名为中文，通过注册从而使page类的变量名变成中文）  
注释：最好在page集合类中添加page的层级关系的注释  

```
#pageaction.py
from page.android_ui.pages.account.add_account_page import Add_Account_Page
class Account:
    add_account=Add_Account_Page()
    def sub_into_account(self,action):
        action.click(self.add_account.account)
    def sub_into_cash(self,action):
        action.click(self.add_account.add)
        action.click(self.add_account.cash)
```
**创建page类**(继承basepage类)，必填属性：name ，实现基类方法：load_android、load_ios
**load_android格式**：  
 ```
from common.page import BasePage
from selenium.webdriver.common.by import By
class Add_Account_Page(BasePage):
    name='添加新账户'

    def load_android(self):
        self.account=self.get_locator('首页账户',By.XPATH, self.button_text("账户"),page='首页')
        self.add = self.get_locator('添加',By.XPATH, self.text_view_desc("添加"),page='账户首页')
        self.cash = self.get_locator('现金', By.XPATH, self.text_view_text("现金"))
        self.account_name=self.get_locator('账户名',By.ID, "com.mymoney:id/name_et", page='账户添加页的账户名')
        self.create=self.get_locator('确认新建',By.XPATH, self.button_text("确认新建"), page='账户添加页的确认新建')
```
**3、编写用例**： 
路径： 项目/test/test_用例组名.py  
**上下文**：  
默认必有py文件 **conftest***，这是pytest运行时的上下文环境（setup、teardown）,导入的base.conftest  
原理通过pytest.fixture装饰器从而不同作用域下实现setup、teardown， 
已加载 初始化环境、driver的运行环境、用例日志  

用例组文件下编写用例集合类(test_用例集名)，编写用例方法（test_用例名）  

**基础用例**：  
```
import allure,pytest
from common.action import ElementActions
from page.android_ui.actions.account import Account
from data.account_casedata import  AccountCaseData as data

@allure.feature("添加账户模块")
@allure.description('账户添加成功')
class Test_Add_Account(Account):
    @allure.story('现金账户名称正常，添加成功')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('account_name',
                             data.addaccount_001.get('params').get('account'))
    def test_addaccount_001(self, action: ElementActions,account_name,):
        self.sub_into_account(action)
        self.sub_into_cash(action)
        # action.input_text(self.add_account.account_name,data.addaccount_001.get('params').get('account'))
        action.input_text(self.add_account.account_name,account_name)
        action.click(self.add_account.create)

    @allure.story('银行卡账户名称正常，添加成功')
    def test_addaccount_002(self, action: ElementActions):
        # action.click(Account.add_account.account)
        self.sub_into_account(action)
        action.click(self.add_account.add)
        action.click(self.add_account.cash)
        action.input_text(self.add_account.account_name, data.addaccount_002.get('params').get('account'))
        action.click(self.add_account.create)
```
**action封装方法原理**：  
click实际就是传入 页面元素参数 ，通过driver.find_element找到后再执行点击事件  
text 通过driver.find_element找到后再执行send_key  
swip_down向下滑动  
is_text_displayed : 判断当前页面是否有对应传参文本  

## 运行方式： 
1、直接运行run.py  
2、run all case:  
    ```python3 run.py```  
run one module case:   
    ```python3 run.py testcase/test_home.py```  
run case with key word:  
    ```python3 run.py -k <keyword>```  
run class case:  
    ```python3 run.py  testcase/test_demo.py::Test_demo```  
run class::method case:  
    ```python3 run.py  testcase/test_demo.py::Test_demo::test_home```  
