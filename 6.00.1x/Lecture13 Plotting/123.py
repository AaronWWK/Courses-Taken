import pylab as plt


plt.figure('My')
plt.plot([1,4,56,32],[1,16,78,90])

plt.figure('You')
plt.plot([1,2,3,4],[1,2,3,44])


plt.figure('My')
plt.ylabel('numbers')
plt.figure('You')
plt.clf()
# plt.title('My')
plt.show()
