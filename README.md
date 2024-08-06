# computorv2

## todo

- [ ] tokenizer + tests
- [ ] remove v1/v2 separation (rename `srcv1`/`srcv2` to `src`)
- [ ] `test_computorvx.py` -> `tests` folder with more files

## general presentation

- [ ] support for rational numbers
- [ ] support for complex numbers
- [ ] support for matrices
- [ ] assignment of an expression to a variable by type inference
- [ ] reassignment of an existing variable with an expression of another type
- [ ] assignment of a variable to another variable (existing or not)
- [ ] resolution of a mathematical expression with defined variables
- [ ] resolution of a mathematical expression without defined variables
- [ ] support and resolution of an equation of degree less than or equal to 2
- [ ] operations between types, as much as possible (???)
- [x] exit the program itself (`exit` or `ctrl+d`)

## assignment part

- [ ] `Rational` type
- [ ] `Imaginary` type (Q^2, not R^2)
- [ ] `Matrix` type (Q^(h\*w), not R^(h\*w))
- [ ] `Function` type with 1 variable

## computational part

- [ ] `+`, `-`,`*`, `/` and `%` operators
- [ ] `^`: exponentiation
- [ ] `**`: matrix multiplication
- [ ] parentheses and computation priorities
- [ ] computations with `= ?` or `?` (???)
- [ ] image computation (function evaluation)
- [ ] equation resolution (Q, R or C) (computorv1)

## syntax part

- [ ] variables only contain letters, are case-insentitive and can't be called `i`
- [ ] at each input validation, you must display the value stored in the variable
- [ ] matrices are defined julia style `matA = [[1,2];[3,2];[3,4]]`
- [ ] functions are defined like so: `fun(var) = ...`

## bonus

- [ ] `Vector` type
- [ ] multiple variables for `Function` type
- [ ] support and resolution of an equation of degree 3
- [ ] `exp`, `sqrt`, `abs`, `cos`, `sin`, `tan`
- [ ] `rad2deg`, `deg2rad`
- [ ] constants: `e`, `pi`, `tau`
- [ ] function composition: `funA(funB(x)) = ?`
- [ ] norm computation
- [ ] display of the list of stored variables and their values
- [ ] history of commands with results
- [ ] matrix inversion
