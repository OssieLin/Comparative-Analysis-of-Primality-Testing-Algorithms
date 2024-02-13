This project is under development, and it's focusing on the comparative analysis of different primality testing algorithms.
Modern cryptography algorithms like RSA or ElGamal need primality tests to generate large random primes. 
For instance, RSA uses the product of two prime numbers to generate the public and private keys; if these primes are predictable, it makes it easier for an attacker to break the encryption scheme. 
Large random primes are constructed in practice by generating pseudorandom numbers and then doing a primality test such as the Fermat primality test or something more powerful such as the Miller–Rabin primality test. 
These primality tests fail for certain numbers called pseudoprimes. 
My research focuses on analyzing the class of Perrin-type primality tests. Dougherty-Bliss and Zeilberger looked at these recently. They find that certain recurrent sequences produce primality tests for which the smallest pseudoprime is very large.
It’s vital to find ways to contribute to modern cryptography with primality tests as the development of quantum computing is posing a great threat to cybersecurity.
