[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tTbZh_rX)
# Introduction to Programming
## Winter Semester 2025/26 — Assignment 10

All concepts required for these tasks have been covered in the lectures and examples.

---

##Problem 1

Consider the system of equations

\( 2x^2 + 3y^2 = r \) and \( y = 2x + 1 \)

where \( r \) is a real parameter

###your task;

Write your code  using **SymPy** that:

-defines the symbolic variables `x`, `y`, and `r`,
- symbolically solve the system for `x` and `y`,
- stores **all solutions** in a list named `sol`,
- where each element of `sol` is a dictionary mapping
  `{x: ..., y: ...}` in terms of the parameter `r`.

Your solution must be **fully symbolic** and must not substitute a numerical value for `r` in this problem.

---

##Problem 2

For the parameter value

\[
r = 10
\]

perform the following tasks;

- plot the ellipse and the line defined in **Problem 1** in the same coordinate system,
- plot the intersection points obtained in **Problem 1** as clearly visible markers,
- label both coordinate axes,
- choose a sensible plotting range,
- save the figure as a pdf file named **`Problem2.pdf`**

This problem will be **graded manually** based on the correctness and clarity of the plot.

Before committing your submission, make sure to add the pdf file to your repository using;

git add Problem2.pdf
