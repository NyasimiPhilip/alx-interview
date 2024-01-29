<h1>Valid UTF-8 Encoding Checker</h1>

<p>This HTML page demonstrates the usage of the Python script for checking valid UTF-8 encoding.</p>

<h2>Usage</h2>

<pre>
<code>
import utf8_checker

# Example data set (list of integers representing bytes)
data_set = [197, 130, 1]

# Check if the data set is a valid UTF-8 encoding
result = utf8_checker.validUTF8(data_set)

# Print the result
print(result)
</code>
</pre>

<p>Replace the <code>data_set</code> variable with your own list of integers representing a data set. The <code>validUTF8</code> function returns <code>True</code> if the data set is a valid UTF-8 encoding; otherwise, it returns <code>False</code>.</p>

<h2>Method Description</h2>

<pre>
<code>
def validUTF8(data):
    """Checks if the data represents a valid UTF-8 encoding.

    Args:
        data (list of integers): List of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    Note:
        A character in UTF-8 can be 1 to 4 bytes long.
        The data set can contain multiple characters.
        Each integer represents 1 byte of data; therefore, you only
        need to handle the 8 least significant bits of each integer.
    """
</code>
</pre>

<h2>Implementation Details</h2>

<p>The <code>validUTF8</code> function iterates through the given data set, examining each byte to determine if it represents a valid UTF-8 encoding. It accounts for ASCII characters (1 byte) and multibyte characters (2 to 4 bytes). The <code>determineNumberOfBytes</code> function assists in identifying the number of bytes in a multibyte character based on the high-order bits of the leading byte.</p>

<h2>Example</h2>

<pre>
<code>
data_set = [197, 130, 1]
result = utf8_checker.validUTF8(data_set)
print(result)  # Output: True
</code>
</pre>

<p>In this example, the data set <code>[197, 130, 1]</code> represents a valid UTF-8 encoding, and the script will print <code>True</code>. Adjust the <code>data_set</code> variable with your own data for testing.</p>
