# from flask import Flask, render_template
# import random
# import numpy as np
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver import ActionChains
# def sigmoid(z):
#   return 1.0/(1 + np.exp(-z))
# def sigmoid_derivative(y):
#   return y * (1.0 - y)
# class NeuralNetwork:
#   def __init__(self, x, y):
#     self.input = x
#     self.weights1 = np.random.rand(self.input.shape[1],4)
#     self.weights2 = np.random.rand(4,4)
#     self.weights3 = np.random.rand(4,1)
#     self.y = y
#     self.output = np.zeros(self.y.shape)
#   def feedforward(self):
#     self.layer1 = sigmoid(np.dot(self.input, self.weights1))
#     self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
#     self.layer3 = sigmoid(np.dot(self.layer2, self.weights3))
#     return self.layer3
#   def backprop(self):
#     delta_3 = 2*(self.y - self.output) * sigmoid_derivative(self.output)
#     d_weights3 = np.dot(self.layer2.T, delta_3)
#     delta_2 = np.dot(delta_3, self.weights3.T) * sigmoid_derivative(self.layer2)
#     d_weights2 = np.dot(self.layer1.T, delta_2)
#     delta_1 =  np.dot(delta_2, self.weights2.T) * sigmoid_derivative(self.layer1)
#     d_weights1 =  np.dot(self.input.T, delta_1)
#     self.weights1 += d_weights1
#     self.weights2 += d_weights2
#     self.weights3 += d_weights3
#   def train(self, x, y):
#     self.output = self.feedforward()
#     self.backprop()
# app = Flask(__name__, template_folder='templates', static_folder='static')
# @app.route('/')
# def base_page():
#   return render_template('index.html')
# @app.route('/mortality/<gender>/<age>/<race>/<state>')
# def mortality(gender, age, race, state):
# #   chrome_options = Options()
# #   chrome_options.add_argument('--no-sandbox')
# #   chrome_options.add_argument('--disable-dev-shm-usage')
# #   browser = webdriver.Chrome(options=chrome_options)
# #   browser.implicitly_wait(30)
# #   browser.maximize_window()
# #   actions = ActionChains(browser)
# #   browser.get('https://alliesagainstcovid.herokuapp.com/')
# #   link = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/section[1]/button")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/div/div/section[1]/div/div/div[1]/div[2]/div/div")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/li[" + gender + "]")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/section[1]/button")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/div/div/section[1]/div/div/div[1]/div[3]/div/div")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/li[" + age + "]")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/section[1]/button")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/div/div/section[1]/div/div/div[1]/div[4]/div/div")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/li[" + race + "]")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/section[1]/button")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/div/div/section[1]/div/div/div[1]/div[5]/div/div")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div/ul/li[" + state + "]")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/section[1]/button")
# #   link.click()
# #   time.sleep(1)
# #   link = browser.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/section[1]/div/div/div[1]/div[13]/div/button")
# #   actions.move_to_element(link).click().perform()
# #   iframe = browser.find_elements_by_tag_name('iframe')[0]
# #   browser.switch_to_frame(iframe)
# #   link = browser.find_element_by_xpath("/html/body/div/label")
# #   output = link.get_attribute("innerText")
#   return "5"#output
# @app.route('/<infectedday>/<contactlast>/<numclass>/<sizeclass>/<numinfect>')
# def home(infectedday, contactlast, numclass, sizeclass, numinfect):
#   dayinfected = int(infectedday)
#   lastcontact = int(contactlast)
#   classnum = int(numclass)
#   classsize = int(sizeclass)
#   infectnum = int(numinfect)
#   maximum = 10
#   totalprob = 1
#   daysince = dayinfected - lastcontact
#   me = 'me'
#   classes = []
#   for i in range(classnum):
#     newclass = []
#     for j in range(classsize):
#       if j == 0 and i < infectnum:
#         newclass.append('infected')
#       else:
#         newclass.append(str(random.randint(1,classnum*classsize)))
#     classes.append(newclass)
#   infected = ['infected']
#   originalinfected = infected
#   classval = []
#   for i in range(len(classes)):
#     newlist = []
#     for j in range(len(classes[i])):
#       newlist.append(0)
#     classval.append(newlist)
#   covidrate = 1.4
#   for i in range(len(classes)):
#     for j in range(len(classes[i])):
#       char = list(classes[i][j])
#       total = 0
#       for q in char:
#         total *= 31
#         total += ord(q)
#       classval[i][j] = total % 10007
#       if classval[i][j] < 0:
#         classval[i][j] += 10007
#   prob = 0
#   maxnum = 0
#   for i in range(len(classes)):
#     if infected[0] in classes[i]:
#       maxnum += len(classes[i])
#   prob = ((covidrate**daysince)/maxnum)%1
#   val1 = prob
#   for i in range(len(classes)):
#     classes[i].append(me)
#   infectedtimes = 1
#   inf0 = []
#   inf1 = []
#   inf2 = []
#   inf3 = []
#   inf4 = []
#   trial = 10000
#   for i in range(trial):
#     infected = originalinfected
#     for day in range(daysince):
#       for idiot in list(set(infected)):
#         for j in range(len(classes)):
#           if idiot in classes[j]:
#             if random.randint(1, trial * covidrate) == 1:
#               inf0.append(random.choice(classes[j]))
#       infected += inf4
#       inf4 = []
#       inf4 += inf3
#       inf3 = []
#       inf3 += inf2
#       inf2 = []
#       inf2 += inf1
#       inf1 = []
#       inf1 += inf0
#       inf0 = []
#     if me in infected:
#       infectedtimes += 1
#   val2 = infectedtimes / (trial)
#   x = np.array(([10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                 [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#                 [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
#                 [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [1, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [2, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [3, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [4, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [5, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [6, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [7, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [8, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [9, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#                 [0, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [1, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [2, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [3, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [4, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [5, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [6, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [7, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [8, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#                 [0, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [1, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [2, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [3, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [4, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [5, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [6, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [7, 8, 8, 8, 8, 8, 8, 8, 8, 8],
#                 [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [1, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [2, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [3, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [4, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [5, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],
#                 [0, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [1, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [2, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [3, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [4, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [5, 6, 6, 6, 6, 6, 6, 6, 6, 6],
#                 [0, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                 [1, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                 [2, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                 [3, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                 [4, 5, 5, 5, 5, 5, 5, 5, 5, 5],
#                 [0, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#                 [1, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#                 [2, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#                 [3, 4, 4, 4, 4, 4, 4, 4, 4, 4],
#                 [0, 3, 3, 3, 3, 3, 3, 3, 3, 3],
#                 [1, 3, 3, 3, 3, 3, 3, 3, 3, 3],
#                 [2, 3, 3, 3, 3, 3, 3, 3, 3, 3],
#                 [0, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#                 [1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
#                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 10],
#                 [0, 1, 2, 3, 4, 5, 6, 7, 9, 10],
#                 [0, 1, 2, 3, 4, 5, 6, 8, 9, 10],
#                 [0, 1, 2, 3, 4, 5, 7, 8, 9, 10],
#                 [0, 1, 2, 3, 4, 6, 7, 8, 9, 10],
#                 [0, 1, 2, 3, 5, 6, 7, 8, 9, 10],
#                 [0, 1, 2, 4, 5, 6, 7, 8, 9, 10],
#                 [0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
#                 [0, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                 [2, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#                 [1, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#                 [1, 1, 2, 3, 4, 5, 6, 7, 8, 10],
#                 [1, 1, 2, 3, 4, 5, 6, 7, 9, 10],
#                 [1, 1, 2, 3, 4, 5, 6, 8, 9, 10],
#                 [1, 1, 2, 3, 4, 5, 7, 8, 9, 10],
#                 [1, 1, 2, 3, 4, 6, 7, 8, 9, 10],
#                 [1, 1, 2, 3, 5, 6, 7, 8, 9, 10],
#                 [1, 1, 2, 4, 5, 6, 7, 8, 9, 10],
#                 [1, 1, 3, 4, 5, 6, 7, 8, 9, 10],
#                 [0, 0, 1, 2, 3, 4, 5, 6, 7, 8],
#                 [0, 0, 1, 2, 3, 4, 5, 6, 7, 9],
#                 [0, 0, 1, 2, 3, 4, 5, 6, 8, 9],
#                 [0, 0, 1, 2, 3, 4, 5, 7, 8, 9],
#                 [0, 0, 1, 2, 3, 4, 6, 7, 8, 9],
#                 [0, 0, 1, 2, 3, 5, 6, 7, 8, 9],
#                 [0, 0, 1, 2, 4, 5, 6, 7, 8, 9],
#                 [0, 0, 1, 3, 4, 5, 6, 7, 8, 9],
#                 [0, 0, 2, 3, 4, 5, 6, 7, 8, 9],
#                 [0, 0, 2, 3, 4, 5, 6, 7, 8, 10],
#                 [0, 0, 2, 3, 4, 5, 6, 7, 9, 10],
#                 [0, 0, 2, 3, 4, 5, 6, 8, 9, 10],
#                 [0, 0, 2, 3, 4, 5, 7, 8, 9, 10],
#                 [0, 0, 2, 3, 4, 6, 7, 8, 9, 10],
#                 [0, 0, 2, 3, 5, 6, 7, 8, 9, 10],
#                 [0, 0, 2, 4, 5, 6, 7, 8, 9, 10],
#                 [0, 0, 3, 4, 5, 6, 7, 8, 9, 10]), dtype=float)
#   y = np.array(([10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [10],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [9],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [0],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1],
#                 [1]), dtype=float)
#   maximum = maximum/2
#   for i in range(len(x)):
#     x[i] = (x[i] - maximum)/maximum
#   for i in range(len(y)):
#     y[i] = (y[i] - maximum)/maximum
#   NN = NeuralNetwork(x,y)
#   length = 10000
#   for i in range(length):
#     NN.train(x, y)
#   for i in range(len(classval)):
#     for j in range(len(classval[i])):
#       classval[i][j] = (classval[i][j]-503)/503
#   new = np.array((), dtype=float)
#   selectlist = []
#   for i in range(10):
#     selectlist.append(classval[random.randint(0, len(classval) - 1)][random.randint(0, len(classval[0]) - 1)])
#   selectlist = np.sort(selectlist)
#   new = np.append(new, selectlist, axis=0)
#   NN.input = new
#   val3 = (NN.feedforward() * maximum + maximum - 1)/10
#   totalprob = totalprob * (((val1 * val2 * val3 + 0.01)**(0.333)) + 0.01)
#   return str((totalprob[0] % 1) * 100)[:5]
# if __name__ == "__main__":
#   app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Sammy!'
