<h1>Metrics Calculator</h1>
<p>This Python script reads from standard input and computes metrics. After every ten lines or the input of a keyboard interruption (CTRL + C), it prints the following statistics:</p>
<ul>
    <li>Total file size up to that point.</li>
    <li>Count of read status codes up to that point.</li>
</ul>

<h2>Usage</h2>
<p>To use this script, run it in your terminal with standard input. It will continuously read lines and calculate metrics. Press CTRL + C to interrupt and display the accumulated statistics.</p>

<h2>Script Overview</h2>

<h3>Function: <code>print_stats(size, status_codes)</code></h3>
<p><strong>Description:</strong><br>
The <code>print_stats</code> function prints accumulated metrics, including the total file size and count of status codes.</p>

<p><strong>Arguments:</strong><br>
<code>size (int)</code>: The accumulated read file size.<br>
<code>status_codes (dict)</code>: The accumulated count of status codes.</p>

<h3>Main Script:</h3>
<pre>
<code>#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
</code>
</pre>