 <h1>Introduction</h1>
    <p>This Python script implements a game where Maria and Ben compete based on prime numbers. The game consists of several rounds, each round involving a list of numbers. The goal is to determine the winner of each round based on certain rules related to prime numbers.</p>
    
    <h1>Usage</h1>
    <p>To use this script, ensure you have Python 3 installed on your system. You can run the script from the command line:</p>
    <code>python prime_game.py</code>
    
    <h1>Functionality</h1>
    <p>The script defines the following functions:</p>
    <ul>
        <li><code>isWinner(x, nums)</code>: This function takes two parameters:
            <ul>
                <li><code>x</code>: An integer representing the number of rounds to be played.</li>
                <li><code>nums</code>: A list of integers representing the numbers for each round.</li>
            </ul>
            It returns the winner of the game overall or None if the input is invalid.
        </li>
        <li><code>rm_multiples(ls, x)</code>: This helper function removes multiples of primes from a list.</li>
    </ul>
    
    <h1>Example</h1>
    <p>Here's an example of how to use this script:</p>
    <pre><code>python
print(isWinner(3, [1, 2, 3]))  # Output: "Maria"
    </code></pre>
    
    <h1>Notes</h1>
    <ul>
        <li>Ensure that the number of rounds x matches the length of the list nums.</li>
        <li>The script assumes valid input and may not handle invalid inputs gracefully.</li>
    </ul>