<h1>README: Solution for "0. Change comes from within"</h1>
<p>This solution provides a Python implementation to solve the coin change problem, specifically addressing the task described in the "0. Change comes from within" project. The objective of this solution is to determine the fewest number of coins needed to meet a given total amount, given a list of coin denominations.</p>

<h2>Functionality:</h2>
<p>The solution contains a single function:</p>

<h3>makeChange(coins, total)</h3>
<p>Parameters:</p>
<ul>
  <li><code>coins</code>: A list of coin denominations.</li>
  <li><code>total</code>: The total amount to be achieved using the given coins.</li>
</ul>
<p>Returns:</p>
<ul>
  <li>The fewest number of coins needed to meet the total.</li>
  <li>If the total is 0 or less, it returns 0.</li>
  <li>If the total cannot be met by any number of coins, it returns -1.</li>
</ul>

<h2>Usage:</h2>
<p>To use this solution, simply call the <code>makeChange()</code> function with appropriate parameters:</p>

<pre><code><span style="color: #0070c1;">result</span> <span style="color: #000000;">=</span> <span style="color: #0070c1;">makeChange</span><span style="color: #000000;">([1, 2, 25], 37)
</span><span style="color: #af00db;">print</span><span style="color: #000000;">(</span><span style="color: #0070c1;">result</span><span style="color: #000000;">)  </span><span style="color: #007f00;"># Output: 7

</span><span style="color: #0070c1;">result</span> <span style="color: #000000;">=</span> <span style="color: #0070c1;">makeChange</span><span style="color: #000000;">([1256, 54, 48, 16, 102], 1453)
</span><span style="color: #af00db;">print</span><span style="color: #000000;">(</span><span style="color: #0070c1;">result</span><span style="color: #000000;">)  </span><span style="color: #007f00;"># Output: -1
</span></code></pre>

<p>In the above examples:</p>
<ul>
  <li>For the list of coin denominations [1, 2, 25] and a total of 37, the fewest number of coins needed is 7.</li>
  <li>For the list of coin denominations [1256, 54, 48, 16, 102] and a total of 1453, it's not possible to meet the total, so the function returns -1.</li>
</ul>

<h2>Implementation Details:</h2>
<ul>
  <li>The function utilizes a greedy algorithm approach to solve the coin change problem.</li>
  <li>It iterates through each coin denomination in descending order and subtracts the coin value from the total as many times as possible, incrementing a counter for each subtraction.</li>
  <li>The process continues until the total is reduced to 0 or cannot be reduced further.</li>
  <li>If the total becomes 0, it means the desired amount has been achieved, and the function returns the count of coins used.</li>
  <li>If the total cannot be met with the given denominations, the function returns -1.</li>
</ul>

<h2>Notes:</h2>
<p>This solution aims for simplicity and efficiency but may not always provide the optimal solution for all sets of coin denominations.</p>