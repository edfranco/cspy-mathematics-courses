# CS-Based Mathematics Curriculum (Algebra 1 and Up)

Source of truth for the course sequence. The editable version lives in a Claude Doc
(see HANDOFF.md for the link); this copy mirrors it as of 2026-10-18.

## How this curriculum works

Nine courses take you from Algebra 1 to the math behind algorithms, graphics, cryptography and
machine learning, with code as the main tool throughout. It is built for self-study by someone
who already programs, so programming is the vehicle and never the subject. Exercises assume
Python, but everything works just as well in TypeScript.

Every course has the same four parts: Topics (in order, with the CS reason for each), Build
(a programming project that cannot be finished without the math), Exit check (what you must be
able to do by hand before moving on), and Resources.

Working rules:

1. Implement every concept. If you can write it from scratch, you understand it.
2. Do it by hand first, then automate it.
3. Write proofs from Course 4 onward.
4. Never skip an exit check. Mastery means 90% or better on a fresh practice set.

About 100 weeks of study in total, which is 24 to 30 months at 6 to 8 hours per week.

## The map

Course 1 (Algebra 1) -> Course 2 (Geometry) -> Course 3 (Algebra 2 and Precalculus), a straight
line. After Course 3, Discrete Math I (4), Linear Algebra (6) and Calculus (7) can run in any
order or two at a time. Course 4 feeds Course 5 (Probability and Statistics). Courses 5, 6 and 7
all feed Course 8 (Discrete Math II), which feeds Course 9 (Electives).

## Course 1: Algebra 1 (10 weeks) -- textbook DONE

| # | Topic | Learn | Why it matters in CS |
|---|---|---|---|
| 1 | Numbers and operations | Integers, rationals, reals, order of operations, absolute value, exponents, roots | Integer vs float, overflow, operator precedence |
| 2 | Expressions | Like terms, distributive property, evaluating and simplifying | Expression trees; simplifying is refactoring |
| 3 | Linear equations | Solving one-variable equations, checking, word problems | Inverting a function; checking is a unit test |
| 4 | Linear functions | Slope, intercept, graphing, rate of change | lerp, easing, mapping ranges |
| 5 | Systems of equations | Substitution, elimination, graphing; none and infinite cases | Constraint solving, line intersection |
| 6 | Inequalities | Linear, compound, absolute value; number line | Bounds checks, clamping, validation |
| 7 | Exponents and growth | Laws of exponents, scientific notation, growth and decay | Binary, powers of 2, big-O doubling |
| 8 | Polynomials | Add, subtract, multiply; factoring | Coefficient arrays, Horner's method |
| 9 | Quadratics | Factoring, completing the square, formula, parabolas | Projectiles, collision timing, maxima |
| 10 | Functions | Domain, range, notation, composition | Pure functions, higher-order functions |

Build: expression evaluator, 2x2 system solver, quadratic solver, plotter.
Exit check: solve any linear equation or inequality and verify; solve a 2x2 system three ways and
explain the none and infinite cases; factor and solve quadratics and derive the quadratic formula;
explain why 2^10 is about 10^3 and why that matters for memory.

## Course 2: Geometry and introductory trigonometry (8 weeks) -- textbook DONE

| # | Topic | Learn | Why it matters in CS |
|---|---|---|---|
| 1 | Logic and proof basics | Conditionals, converse, contrapositive, two-column proofs | Preconditions and invariants |
| 2 | Lines and angles | Parallel lines, angle relationships, angle sums | First deductive chains |
| 3 | Triangles | Congruence, similarity, Pythagorean theorem, triangle inequality | Distance, collision, meshes |
| 4 | Coordinate geometry | Distance, midpoint, slope, lines and circles | Screen coordinates, hit testing |
| 5 | Transformations | Translation, rotation, reflection, scaling, composition | CSS and canvas transforms; sets up matrices |
| 6 | Polygons and area | Area and perimeter formulas, regular polygons | Shoelace formula, rasterization, bounding boxes |
| 7 | Circles | Arcs, chords, tangents, arc length, sectors | Circular motion, radial layouts |
| 8 | Right-triangle trig | Sine, cosine, tangent, inverse trig | Angles to vectors and back |
| 9 | Unit circle and radians | Radians, special angles, trig around the circle | Every graphics and audio API uses radians |
| 10 | Vectors in 2D | Components, magnitude, addition, scaling, dot product | Movement, forces, projection, lighting |

Build: 2D canvas or SVG scene with typed transforms, point-in-polygon, circle-line intersection,
angle readout between two vectors.
Exit check: prove the Pythagorean theorem and the triangle angle sum; convert standard angles
between degrees and radians without a calculator; compute distance, midpoint and dot product and
explain the sign of the dot product; write a function that rotates a point about the origin.

## Course 3: Algebra 2 and Precalculus (12 weeks) -- NEXT

| # | Topic | Learn | Why it matters in CS |
|---|---|---|---|
| 1 | Functions in depth | Graph transformations, inverses, piecewise, even/odd | Inverse mappings, easing curves |
| 2 | Polynomial functions | End behavior, roots, remainder and factor theorems, synthetic division | Root finding, interpolation |
| 3 | Rational functions | Asymptotes, holes, domain restrictions | Division by zero, limits intuition |
| 4 | Radicals and rational exponents | Simplifying, solving radical equations | Roots in distance and normalization |
| 5 | Exponentials and logarithms | Log properties, change of base, solving exponential equations | log n in binary search, log scales, bits |
| 6 | Sequences and series | Arithmetic, geometric, recursive definitions, sigma notation, sum formulas | Recursion, loops, amortized analysis |
| 7 | Complex numbers | Arithmetic, polar form, powers and roots | 2D rotation, signals, fractals |
| 8 | Matrices | Add, multiply, 2x2 and 3x3 determinants, inverses, solving systems | Transforms; preview of Course 6 |
| 9 | Trig beyond right triangles | Law of sines and cosines, identities, trig graphs | Waves, periodic animation, audio |
| 10 | Conic sections | Parabolas, circles, ellipses, hyperbolas | Orbits, collision shapes |
| 11 | Counting preview | Counting principle, permutations, combinations, binomial theorem | Preview of Course 4 |

Build: Mandelbrot renderer with own complex type; sequence explorer with partial sums;
3x3 matrix calculator that solves a system of three equations.
Exit check: solve exponential and log equations and explain why log2(n) counts binary search
steps; turn a recursive sequence into closed form and prove the geometric sum formula; multiply
two 3x3 matrices and compute a 3x3 determinant by hand; convert a complex number to polar form
and multiply in polar form.

## Course 4: Discrete Mathematics I (12 weeks)

Topics: propositional logic; predicate logic; proof techniques (direct, contrapositive,
contradiction, cases, induction); sets; functions and relations; number theory (divisibility,
primes, GCD, Euclidean algorithm, modular arithmetic); counting (sum and product rules,
permutations, combinations, pigeonhole, inclusion-exclusion); recursion and recurrences (intro);
introduction to graphs.
Build: truth table generator and equivalence checker; extended Euclidean algorithm and modular
inverse; combinatorics library tested against brute-force enumeration.
Exit check: induction proofs (sum of first n odd numbers is n^2; recursive function terminates);
negate a statement with two quantifiers; GCD and modular inverse by hand; count passwords with
inclusion-exclusion.

## Course 5: Probability and Statistics (10 weeks)

Topics: descriptive statistics; probability basics; conditional probability and Bayes; discrete
random variables (Bernoulli, binomial, geometric, Poisson); continuous random variables (uniform,
normal, exponential); sampling and the central limit theorem; estimation and confidence intervals;
hypothesis testing; correlation and regression; randomized algorithms and hashing.
Build: Monte Carlo simulator (pi, birthday paradox, quicksort comparisons); A/B test calculator;
naive Bayes text classifier.
Exit check: binomial expectation and variance by hand and by simulation; Bayes on a medical test
with base rates; run and interpret a two-sample test; explain expected hash collisions.

## Course 6: Linear Algebra (12 weeks)

Topics: vectors in n dimensions; matrices as linear maps; Gaussian elimination; vector spaces;
determinants; orthogonality (Gram-Schmidt, QR, least squares); eigenvalues and eigenvectors;
singular value decomposition; 3D graphics math (homogeneous coordinates, rotation matrices,
quaternions intro, projection).
Build: matrix library with no NumPy; 3D wireframe renderer; PageRank on a small graph; image
compression by truncated SVD.
Exit check: row-reduce a 4x4 system; explain and compute eigenvectors of a 2x2; build a rotation
matrix about any axis; derive least squares from the normal equations.

## Course 7: Calculus I and II (16 weeks)

Topics: limits and continuity; derivatives; applications (optimization, Newton's method);
integrals; numerical methods (trapezoid, Simpson, Euler); sequences and series (Taylor);
multivariable basics (partials, gradient); continuous probability; differential equations intro.
Build: forward-mode autodiff library; gradient descent optimizer fitting a line then a tiny
network; pendulum simulator comparing Euler and Runge-Kutta.
Exit check: differentiate and integrate standard functions; state and explain the fundamental
theorem; derive the Taylor series of e^x and bound the error; implement gradient descent from the
definition.

## Course 8: Discrete Mathematics II, the math of algorithms (12 weeks)

Topics: asymptotic analysis; recurrences (master theorem); graph theory; trees; number theory for
cryptography (Fermat, Euler, CRT, primality tests); combinatorics II (generating functions,
Catalan numbers); Boolean algebra and circuits; formal languages and automata; computability and
complexity intro.
Build: RSA from scratch with Miller-Rabin; regex engine compiling to NFA then DFA; recurrence
solver verified empirically.
Exit check: prove O(n log n) by master theorem and recursion tree; prove a graph with n vertices
and n edges contains a cycle; explain RSA via Euler's theorem; convert a regex to a DFA by hand.

## Course 9: Electives and capstone (8 to 12 weeks, pick two)

Math of machine learning; numerical analysis; computer graphics math; optimization; theory of
computation and logic; applied cryptography. Each with a capstone (e.g. MNIST network from
scratch, FFT spectrum visualizer, software ray tracer, bin-packing solver, typed lambda calculus
interpreter, elliptic curve Diffie-Hellman).

## Resources (standard picks, check current editions)

- Algebra 1: AoPS Introduction to Algebra; Khan Academy
- Geometry: AoPS Introduction to Geometry; Khan Academy
- Algebra 2 / Precalc: Stitz and Zeager Precalculus (free); Khan Academy
- Discrete I: Levin, Discrete Mathematics: An Open Introduction (free); MIT 6.042J
- Probability: Blitzstein and Hwang; Harvard Stat 110; OpenIntro Statistics (free)
- Linear Algebra: Strang; MIT 18.06; 3Blue1Brown Essence of Linear Algebra
- Calculus: Strang Calculus (free) or OpenStax; 3Blue1Brown Essence of Calculus
- Discrete II: Concrete Mathematics; Sipser; MIT 6.006
- Electives: Mathematics for Machine Learning (free); Trefethen and Bau; Lengyel; Ray Tracing in
  One Weekend (free); Serious Cryptography; Boneh and Shoup (free)
- Practice: Project Euler (Courses 3 to 8); AoPS Alcumus (Courses 1 to 3)

## Pacing and study method

6 to 8 hours a week in four or five sessions: read and work examples (2h), hand practice (2h),
build (2h), review (1h). Mastery rules: 90% on a fresh set before moving on; keep a mistake log;
write proofs in full sentences; when stuck 20 minutes, read the solution and reproduce it the
next day; review at one week, one month, three months.
