Start tests execution:
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features

Generates allure report:
allure generate allure/results/ -o allure/reports --clean

Note take a look on generated XLM report in "reports" folder