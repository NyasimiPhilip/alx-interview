  <h1>Island Perimeter Problem</h1>
    <p>This Python script island_perimeter.py provides a solution to the island perimeter problem. It calculates the perimeter of an island described in a grid of 0s (water) and 1s (land).</p>
    <h2>Problem Statement</h2>
    <p>Given a 2D grid representing an island, where 1 represents land and 0 represents water, calculate the total perimeter of the island. The grid is surrounded by water, and there is exactly one island.</p>
    <p>The perimeter is the total length of the boundaries of the island.</p>
    <h2>Usage</h2>
    <h3>Running the Script</h3>
    <p>To use the island_perimeter.py script, simply provide a 2D list of integers representing the island grid. The script will calculate the perimeter of the island and return the result.</p>
    <p><strong>Example usage:</strong></p>
    <pre><code>python3 island_perimeter.py</code></pre>
    <h3>Function: island_perimeter(grid)</h3>
    <p>The island_perimeter function takes a single argument grid, which is a 2D list of integers representing the island grid. It calculates the perimeter of the island described in the grid and returns the result.</p>
    <h4>Arguments</h4>
    <p><em>grid:</em> A 2D list of integers containing 0 (water) or 1 (land).</p>
    <h4>Returns</h4>
    <p>The perimeter of the island as an integer.</p>
    <h3>Example</h3>
    <p>Consider the following island represented by the grid:</p>
    <pre><code>[
 [0, 1, 0, 0],
 [1, 1, 1, 0],
 [0, 1, 0, 0],
 [1, 1, 0, 0]
]</code></pre>
    <p>The perimeter of this island is 16. You can calculate it using the island_perimeter function provided in this script.</p>