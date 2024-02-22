 <h1>Rotate 2D Matrix</h1>

  <h2>Problem Statement</h2>
  <p>Given an n x n 2D matrix, rotate it 90 degrees clockwise.</p>

  <h2>Prototype</h2>
  <pre><code>def rotate_2d_matrix(matrix):
    pass
  </code></pre>

  <p><strong>Do not return anything.</strong> The matrix must be edited in-place.</p>
  <p>You can assume the matrix will have 2 dimensions and will not be empty.</p>

  <h2>Example</h2>

  <pre><code>matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
</code></pre>

  <p><strong>Output:</strong></p>
  <pre><code>[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
</code></pre>

  <h2>Approach</h2>
  <p>To rotate the matrix 90 degrees clockwise, we can perform two steps:</p>
  <ol>
    <li>Transpose the matrix: Swap elements across the  main diagonal(top left to bottom right).</li>
    <li>Reverse each row: Reverse the elements in each row.</li>
  </ol>
