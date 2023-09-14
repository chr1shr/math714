# Introductory examples
This directory contains several introductory examples used in lectures 1 and 2.

## The deriv.py example
The **deriv.py** tests the accuracy of the second-order finite-difference
formula that was derived in the lectures. It tests the formula for a range of
step sizes *h*. The program can be run by typing the following command in the
terminal:
```Shell
python3 deriv.py
```
The program outputs the results to the terminal. Each line contains the step
size *h*, the numerical derivative, the exact derivative, and the magnitude of
the absolute error. The results can be saved to a temporary file by using the
`>` operator to redirect the output:
```Shell
python3 deriv.py >out
```
This will create a file called **out** that contains the same data that was
displayed on the terminal.

## Plotting the results
This data file is ideal for use with
[Gnuplot](http://www.gnuplot.info), a freeware graphing utility that is widely
used and available on many computing platforms. Gnuplot can work with many
types of input data in both text and binary formats. It can produce
high-quality output for publications, and provides a simple interface
for performing subsequent computations.

In Gnuplot, the following commands will plot the magnitude of the absolute error
as a function of the step size:
```Gnuplot
set xlabel 'h'
set ylabel 'Magnitude of abs. error'
unset key
plot 'out' using 1:4 with linespoints
```
The final `plot` command will using column 1 (containing *h*) and column 4
(containing the magnitude of absolute error). Many commands in Gnuplot can be
abbreviated. For example, the plotting command can be written equivalently as
```Gnuplot
plot 'out' u 1:4 w lp
```
The graph of the results is difficult to interpret, because the values of **h** span
many orders of magnitude. A clearer view is achieved by using logartihmic axes, using the following commands:
```Gnuplot
set logscale xy
plot 'out' u 1:4 w lp
```
For *h* larger than 10<sup>-5</sup>, the data appears to follow a quadratic
scaling behavior, as expected for a second-order scheme. For *h* smaller than
10<sup>-5</sup> numerical roundoff errors dominate and the results become less
accurate.

## Fitting a power law model
A power law scaling for the error corresponds to linear scaling in the
logarithmic plot. Gnuplot can be used to fit the data for *h* &gt;
10<sup>-5</sup> with linear regression, using the following commands:
```Gnuplot
f(x)=a*x+b
fit [log(1e-5):*] 'out' u (log($1)):(log($4)) via a,b
```
The section `(log($1)):(log($4))` tells Gnuplot to fit the line to the
logarithms of the data in columns 1 and 4. The initial section `[log(1e-5):*]`
tells the fitting procedure to be limited to the data with *h* &gt;
10<sup>-5</sup>, where the additional `log` is incorporated since the raw
numbers in the data file are being transformed by the `log` already. The
fitting procedure finds that *a* = 2.02 and *b* = -0.451. As expected, *a* is
close to 2, consistent with quadratic scaling. The results can be overlaid
on the plot using the following commands:
```Gnuplot
set key top left
plot [1e-5:*] exp(f(log(x))) w l t 'Power law fit', 'out' u 1:4 w p pt 7 t 'Data'
```
The same procedure could be used to fit many other types of numerical
convergence data. Note that it is up the user to determine the appropriate
range over which to fit the results. In this example, it would *not* be appropriate
to perform linear regression over all the data, using the following commands:
```Gnuplot
fit 'out' u (log($1)):(log($4)) via a,b
plot exp(f(log(x))) w l t 'Power law fit', 'out' u 1:4 w p pt 7 t 'Data'
```
In this case, the line fits the data poorly. Here *a* is computed as 0.472,
since the regime dominated by rounding error obscures the quadratic scaling.
