# Comparative Analysis of Lucas-Type Sequence
## Intro
Modern cryptography algorithms like RSA need primality tests to generate large random primes.\
Specifically, RSA uses the product of two prime numbers to generate the public and private keys; if these primes are predictable, it makes it easier for an attacker to break the encryption scheme.\
\
Large random primes are constructed in practice by generating pseudorandom numbers and then doing a primality test such as the Fermat primality test or something more powerful such as the Miller–Rabin primality test.\
These primality tests fail for certain numbers called **pseudoprimes**.\
My research focuses on analyzing the class of Perrin-type primality tests- **Lucas-Type Sequence**:

## [Lucas-Type Sequence](https://oeis.org/wiki/Lucas_sequences)
Each primality test is a sequence with two parameters($$c_0, c_1$$):
$$V_{n+2} = c_1 V_{n+1} + c_0 V_{n}, \quad V_{0} = 2, \quad V_{1} = c_1$$

If p is prime, then we have the congruence $$V_{p}\equiv V_{1}(mod\quad p)$$

### Method 
Visualize the quality of primality tests through **the number of pseudoprimes up to N** and **the sizes of the smallest pseudoproimes**.
Analyze the extreme cases that stand out from the visulizations and try to find patterns among them.

### Conclusion
A lot of pseudoprimes are divisible by 2 and 3, and thus we can improve the primality tests by adding a condition to restrict to 3 rough numbers after each primality test.
