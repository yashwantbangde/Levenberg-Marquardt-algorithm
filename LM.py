import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def quadratic_function(x, a, b, c):
    """
    Quadratic function
    """
    return a * x**2 + b * x + c

def jacobian_quadratic(x, a, b, c):
    """
    Jacobian matrix for quadratic function
    """
    jacobian = np.zeros((len(x), 3))
    jacobian[:, 0] = x**2
    jacobian[:, 1] = x
    jacobian[:, 2] = 1
    return jacobian

def levenberg_marquardt_quadratic(x, y, a_init, b_init, c_init, lmbda_init, tol, max_iter):
    """
    Levenberg-Marquardt algorithm for quadratic function
    """
    # Initial values
    a = a_init
    b = b_init
    c = c_init
    lmbda = lmbda_init
    
    # Iterations
    for i in range(max_iter):
        # Compute residual
        r = y - quadratic_function(x, a, b, c)
        
        # Compute Jacobian matrix
        jacobian = jacobian_quadratic(x, a, b, c)
        
        # Compute Hessian matrix
        hessian = np.dot(jacobian.T, jacobian)
        
        # Add damping parameter to diagonal of Hessian matrix
        hessian += lmbda * np.diag(np.diag(hessian))
        
        # Compute step
        step = np.linalg.solve(hessian, np.dot(jacobian.T, r))
        
        # Update parameters
        a += step[0]
        b += step[1]
        c += step[2]
        
        # Compute new residual
        r_new = y - quadratic_function(x, a, b, c)
        
        # Compute new objective function value
        obj_new = np.sum(r_new**2)
        
        # Check for convergence
        if abs(obj_new - np.sum(r**2)) < tol:
            break
        
        # Adjust damping parameter
        if obj_new < np.sum(r**2):
            lmbda /= 10
        else:
            lmbda *= 10
            
    return a, b, c

# User input sliders
a_init = st.slider('Initial value of a', min_value=-10.0, max_value=10.0, step=0.1, value=-2.0)
b_init = st.slider('Initial value of b', min_value=-10.0, max_value=10.0, step=0.1, value=3.0)
c_init = st.slider('Initial value of c', min_value=-10.0, max_value=10.0, step=0.1, value=1.0)
lmbda_init = st.slider('Initial value of lambda', min_value=0.0, max_value=100.0, step=0.1, value=1.0)
tol = st.slider('Tolerance', min_value=1e-8, max_value=1e-1, step=1e-8, value=1e-6)
max_iter = st.slider('Maximum number of iterations', min_value=1, max_value=1000, step=1, value=100)
x = np.linspace(-10, 10, 100)
y = quadratic_function(x, a_init, b_init, c_init)
y_noise = y + np.random.normal(0, 1, len(y))
a_opt, b_opt, c_opt = levenberg_marquardt_quadratic(x, y_noise, a_init, b_init, c_init, lmbda_init, tol, max_iter)

fig, ax = plt.subplots()
ax.scatter(x, y_noise, s=10, label='Noisy data')
ax.plot(x, y, label='True function')
ax.plot(x, quadratic_function(x, a_opt, b_opt, c_opt), label='Optimized function')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Quadratic function optimization')
st.pyplot(fig)


