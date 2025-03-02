import numpy as np
from scipy.optimize import minimize

class DDFOptimizer:
    def __init__(self, X, Y, B):
        """
        initiate Directional Distance Function (DDF) optimizer
        :param X: np.array, input
        :param Y: np.array, good output
        :param B: np.array, bad output
        """

        self.X = X
        self.Y = Y
        self.B = B
        self.num_dmu = X.shape[1]  
        self.num_input = X.shape[0]  
        self.num_good = Y.shape[0]  
        self.num_bad = B.shape[0]  

    def solve_ddf_for_dmu(self, dmu_index):
        """
        calculate distance for a specific DMU
        :param dmu_index: index of DMU
        :return: result
        """
        x0 = self.X[:, dmu_index]
        y0 = self.Y[:, dmu_index]
        b0 = self.B[:, dmu_index]

        g_x, g_y, g_b = x0.copy(), y0.copy(), b0.copy()

        init_vars = np.zeros(self.num_dmu + 1)
        init_vars[:self.num_dmu] = 1.0 / self.num_dmu  
        init_vars[self.num_dmu] = 0.0  

        def objective(vars):
            return -vars[self.num_dmu]

        constraints = []
        for i in range(self.num_input):
            constraints.append({'type': 'ineq', 'fun': lambda vars, i=i: x0[i] - np.dot(self.X[i, :], vars[:self.num_dmu]) - vars[self.num_dmu] * g_x[i]})
        for k in range(self.num_good):
            constraints.append({'type': 'ineq', 'fun': lambda vars, k=k: np.dot(self.Y[k, :], vars[:self.num_dmu]) - y0[k] - vars[self.num_dmu] * g_y[k]})
        for l in range(self.num_bad):
            constraints.append({'type': 'eq', 'fun': lambda vars, l=l: np.dot(self.B[l, :], vars[:self.num_dmu]) + vars[self.num_dmu] * g_b[l] - b0[l]})

        bounds = [(0, None)] * (self.num_dmu + 1)

        result = minimize(objective, init_vars, method='SLSQP', bounds=bounds, constraints=constraints, options={'ftol': 1e-4, 'maxiter': 1e5, 'disp': False})

        return result

    def solve_all(self):
        """
        calculate all DMU distance
        :return: results
        """
        results = {}
        for j in range(self.num_dmu):
            res = self.solve_ddf_for_dmu(j)
            results[f"DMU{j+1}"] = {"theta": res.x[self.num_dmu], "success": res.success, "message": res.message}
        return results
