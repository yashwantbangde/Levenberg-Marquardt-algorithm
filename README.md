# Implementation of Levenberg-Marquardt algorithm from scratch

1. The code begins by importing the required libraries - NumPy, Matplotlib, and Streamlit.

2. The quadratic_function function takes in x, a, b, and c as input parameters and returns the output of the quadratic function. This function simply computes the output of the quadratic function for the given input values of x, a, b, and c.

3. The jacobian_quadratic function takes in x, a, b, and c as input parameters and returns the Jacobian matrix for the quadratic function. This function computes the Jacobian matrix for the given input values of x, a, b, and c by setting the first column of the Jacobian matrix as x**2, the second column as x, and the third column as 1.

4. The levenberg_marquardt_quadratic function takes in x, y, a_init, b_init, c_init, lmbda_init, tol, and max_iter as input parameters and implements the Levenberg-Marquardt algorithm to optimize the quadratic function. The function initializes the parameter values as a = a_init, b = b_init, c = c_init, and lambda = lambda_init.

5. The for loop in levenberg_marquardt_quadratic iterates over max_iter iterations to optimize the quadratic function.

6. The first step in each iteration is to compute the residual, r, which is the difference between the actual output of the quadratic function and the observed output of the quadratic function for the given input values of x.

7. The next step is to compute the Jacobian matrix for the current parameter values of a, b, and c using the jacobian_quadratic function.

8. The Hessian matrix is computed by taking the dot product of the transpose of the Jacobian matrix and the Jacobian matrix itself.

9. The damping parameter, lambda, is added to the diagonal elements of the Hessian matrix.

10. The step size, step, is computed by solving the linear system Hessian * step = Jacobian^T * residual, where ^T denotes the transpose of a matrix.

11. The parameter values a, b, and c are updated using the computed step size.

12. The new residual, r_new, and the new objective function value, obj_new, are computed using the updated parameter values.

13. The algorithm checks for convergence by computing the absolute difference between the new and old objective function values and comparing it to the user-defined tolerance, tol. If the difference is less than the tolerance, the algorithm has converged and the break statement is executed to exit the loop.

14. If the new objective function value is less than the old objective function value, the damping parameter is decreased by a factor of 10. Otherwise, the damping parameter is increased by a factor of 10.

15. Finally, the optimized parameter values a_opt, b_opt, and c_opt are returned by the function.

16. The next few lines of code create sliders for the user to adjust the initial parameter values, damping parameter, tolerance, and maximum number of iterations.

17. The x values for plotting are generated using np.linspace.

18. The y values for the true function and the y_noise values for the noisy data are computed using the quadratic_function
