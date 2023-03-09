# Generate Local Python File for LeetCode Problems

For online LeetCode users who wish to work on and store code offline, this script reads a problem-specific URL and:
- Queries problem information from LeetCode (LeetCode uses GraphQL as it's API query language)
- Creates a local Python file with the appropriate file name
- Formats and adds the problem information
- Launches the new file to be worked on (Windows function only)

Usage:
1. In the terminal, navigate to the directory where you intend to generate the new Python file
2. Acquire the full URL of the LeetCode problem to use as argument  (ex: 'https://leetcode.com/problems/same-tree/' or 'https://leetcode.com/problems/same-tree/description/')
3. Run main.py <URL>  (ex: main.py https://leetcode.com/problems/same-tree/description/)

Sample LeetCode problem from website:
![alt text](https://github.com/justinliu1308/create-python-file-leetcode/blob/main/sample-problem-screenshot.png)

Sample output file created:
![alt text](https://github.com/justinliu1308/create-python-file-leetcode/blob/main/output-screenshot.png)
