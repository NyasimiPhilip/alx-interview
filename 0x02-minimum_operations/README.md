<h1>0x02. Minimum Operations</h1>
<p>
This Python script defines a function minOperations that calculates the fewest number of operations needed to result in exactly n H characters in a file. The script also includes a helper function primeFactorization that returns the prime factorization elements of a given number<p>
<h2>Function 1: primeFactorization(x)</h2>
<p><strong>Description:</strong><br>
The <code>primeFactorization</code> function takes an integer x as input and returns a list containing the prime factorization elements of x.</p>

<p><strong>Algorithm:</strong><br>
The function initializes a variable <code>div</code> to 2 and an empty list <code>array</code>.<br>
It then enters a while loop where it checks if <code>div</code> is less than or equal to <code>x</code>.<br>
Inside the loop, it checks if <code>x</code> is divisible by <code>div</code>.<br>
If true, it appends <code>div</code> to the array and updates <code>x</code> by dividing it by <code>div</code>.<br>
If false, it increments <code>div</code> by 1.<br>
The loop continues until <code>div</code> is greater than <code>x</code>.<br>
The function returns the array containing prime factorization elements.</p>

<p><strong>Example:</strong><br>
For <code>x = 12</code>, the prime factorization is <code>[2, 2, 3]</code>.</p>

<h2>Function 2: minOperations(n)</h2>
<p><strong>Description:</strong><br>
The <code>minOperations</code> function calculates the fewest number of operations needed to result in exactly <code>n</code> H characters in a file.</p>

<p><strong>Algorithm:</strong><br>
The function initializes a variable <code>min</code> to 0.<br>
It uses the <code>primeFactorization</code> function to obtain a list of prime factorization elements of <code>n</code>.<br>
It then creates a dictionary <code>occurrences</code> to store the count of each prime factor.<br>
Using a for loop, it iterates over the items (prime factors) in <code>occurrences</code> and calculates the minimum number of operations by adding the product of the prime factor and its count (<code>k * v</code>) to <code>min</code>.<br>
The function returns the calculated minimum number of operations.</p>
<p><strong>Example:</strong><br>
For <code>n = 12</code>, the prime factorization is <code>[2, 2, 3]</code>.<br>
The <code>occurrences</code> dictionary is <code>{2: 2, 3: 1}</code>, and the minimum number of operations is <code>2 * 2 + 3 = 7</code>.</p>