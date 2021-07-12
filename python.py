import matplotlib.pyplot as plt
import charts

figure = plt.figure()
axes = figure.add_subplot(1,1,1)
axes.bar([1,2,3,4],[3,5,7,25],tick_label = ["A","B","C","D"])
plt.show()
