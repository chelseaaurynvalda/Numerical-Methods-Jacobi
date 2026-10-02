#GAUSS-SEIDEL METHOD

# Initial guess
x = y = z = 0.0

tolerance = 0.01
max_iterations = 100

print("Gauss-Seidel Iteration")
print("Iterasi      x          y          z         Error (%)")

for i in range(1, max_iterations + 1):
    x_new = (15 - 2*y + z) / 12
    y_new = (-18 + 2*x_new - 3*z) / (-10)
    z_new = (22 - x_new - 2*y_new) / 8

    error_x = abs((x_new - x) / x_new) * 100 if x_new != 0 else 0
    error_y = abs((y_new - y) / y_new) * 100 if y_new != 0 else 0
    error_z = abs((z_new - z) / z_new) * 100 if z_new != 0 else 0
    error = max(error_x, error_y, error_z)

    print(f"{i:3d}   {x_new:.6f}   {y_new:.6f}   {z_new:.6f}   {error:.6f}")

    x, y, z = x_new, y_new, z_new

    if error < tolerance:
        break

print("\nHasil akhir:")
print("x =", x)
print("y =", y)
print("z =", z)
print("Iterasi =", i)