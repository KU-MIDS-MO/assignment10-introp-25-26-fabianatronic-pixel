import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y, r = sp.symbols ('x y r', real=True)

eq1 = sp.Eq(2*x**2 + 3*y**2, r)
eq2 = sp.Eq(y,2*x +1)

sol= sp.solve ([eq1, eq2], [x, y], dict = True)

r_val = 10  #set the parameter value

pts = []         #create an empty list to store point coordinates.
for s in sol:    #loop over each symbolic solution s inside sol (there are 2).
    xv =sp.N(s[x].subs(r,r_val))
    #s[x]= take the x expression from solution s
    #.subs(r, r_val) = substitute r with 10
    #sp.N = then numerically evaluate it. 
    yv =sp.N(s[x].subs(r,r_val))
    pts.append((float(xv), float(yv)))
    #pts.append(...) = append to pts (add to thhe the end)
    #( ... , ... ) = a tuple (x, y)
    #float(xv) = converted to Python floats.
    
t= np.linspace(0.2*np.pi, 800)  #np.linspace(start, stop, num) creates num points with the same distance between
a= float (sp.sqrt(r_val/2))  #x semi-axis of the ellipse
#sp.sqrt = symbolic square root
b= float (sp.sqrt(r_val/3))  #y semi-axis: 

xe = a*np.cos(t)  #ellipse x-coordinates (la formula sarebbe a cos t)
ye = b*np.sin(t)  #ellipse y-coordinates

xline =np.linspace(-3,3,400)   #choose an x-range to draw the line (400 points
yline = 2*xline + 1            #commpute y=2x+1 for all x values

plt.figure(figsize =(7,5))   #create a figure canvas sized 7×5 inches.(pollici)
plt.plot(xe, ye, label = r'$2x^2 + 3y^2 = 10$')  #plot the ellipse points and assign a legend label.
#plt.plot(x, y, ...) = plot di una curva
#???
plt.plot(xline, yline, label = r'$y =2x +1$')

px, py = zip(*pts) #unzip point pairs into x-coordinates and y-coordinates
                   #* separate the list values
plt.scatter (px, py, s=70, marker='o', label='intersections')
#draw intersection points as markers; s=70 makes them clearly visible, it's the marker dimension

plt.axhline (0, linewidth= 0.8)   
plt.axvline (0, linewidth= 0.8)    
plt.xlabel('x')   # #label x-axis. (etichetta)
plt.ylabel('y')   #label y-axis 
plt.title('problem 2 : Ellipse and line with intersection points')
plt.legend()   #show legend.
plt.grid(True, alpha =0.3)    #light grid (alpha transparency).

plt.xlim(-3,3)    #set x range from -3 to 3
plt.ylim (-3,6)   #set y range from -3 to 6.

plt.savefig('Problem2.pdf', bbox_inches= 'tight')
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(script_dir , "Problem2.pdf")
plt.savefig(out_path, bbox_inches= "tight")
print("Save to:", out_path)


plt.show()   #display the figure.
plt.close()  #close the figure to free resources.

#%%
#For the parameter value

#\[
#r = 10
#\]

#perform the following tasks;

#- plot the ellipse and the line defined in **Problem 1** in the same coordinate system,
#- plot the intersection points obtained in **Problem 1** as clearly visible markers,
#- label both coordinate axes,
#- choose a sensible plotting range,
#- save the figure as a pdf file named **`Problem2.pdf`**

#This problem will be **graded manually** based on the correctness and clarity of the plot.

#Before committing your submission, make sure to add the pdf file to your repository using;

#git add Problem2.pdf

#%%


