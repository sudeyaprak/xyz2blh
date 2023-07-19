# xyz2blh

### Cartesian coordinates (𝑥, 𝑦, 𝑧) to ellipsoidal coordinates (𝜑, 𝜆, ℎ)

<img width="700" alt="image" src="https://github.com/sudeyaprak/xyz2blh/assets/119863892/2f02fbe2-8d59-45bd-a8c7-6fce57cb17e5">

The code performs a coordinate conversion from Cartesian coordinates to ellipsoidal coordinates using the GRS80 ellipsoid model. Here's a description of the code and its purpose:

1. User Input:
   - The code prompts the user to enter the X, Y, and Z coordinates of a point in the Cartesian coordinate system.
   - The `input()` function is used to obtain these values from the user, and the `float()` function is used to convert the input to floating-point numbers.

2. GRS80 Ellipsoid Parameters:
   - The code defines the parameters of the GRS80 ellipsoid, which is a mathematical representation of the Earth's shape.
   - The semi-major axis (`a`) is set to 6378137.0 meters.
   - The semi-minor axis (`b`) is set to 6356752.3141 meters.

3. Conversion Function `xyz2blh`:
   - The code defines a function named `xyz2blh` that takes the Cartesian coordinates (`x`, `y`, `z`) as input and performs the conversion to ellipsoidal coordinates.
   - Inside the function, various calculations are performed to determine the longitude, latitude, and height of the point.

4. Eccentricity Calculation:
   - The code calculates the eccentricity (`e`) of the GRS80 ellipsoid using the provided formula, which is based on the semi-major and semi-minor axes.

5. Longitude Calculation:
   - The code calculates the longitude (`λ`) using the `atan2()` function, which returns the arc tangent of `y` divided by `x`.
   - The resulting value is converted from radians to degrees using

Output should be like

```python
X coordinate:4210520.621
Y coordinate:1128205.600
Z coordinate:4643227.496
Cartesian coordinates (𝑥, 𝑦, 𝑧) to ellipsoidal coordinates (𝜑, 𝜆, ℎ):
(14.999999998583872, 47.00006024239489, 2007.184077466838)
```python
