# Generate Local Python File for LeetCode Problems

For online LeetCode users who wish to work on and save code offline, this script reads a URL with the specific problem and:
- Queries problem information from LeetCode (LeetCode uses GraphQL as its API query language)
- Creates a local Python file with the appropriate file name if file does not already exist
- Formats and populates the problem information
- Launches the new file to be worked on (Windows function only)

Usage:
1. In the terminal, navigate to the directory where you intend to generate the new Python file
2. Acquire the full URL of the LeetCode problem to use as argument  (ex: 'https://leetcode.com/problems/same-tree/' or 'https://leetcode.com/problems/same-tree/description/')
3. Run main.py <URL>  (ex: `main.py https://leetcode.com/problems/same-tree/description/`)

Sample LeetCode problem from website:
![alt text](https://github.com/justinliu1308/create-python-file-leetcode/blob/main/img/sample-problem-screenshot.png)

Sample output file created:
![alt text](https://github.com/justinliu1308/create-python-file-leetcode/blob/main/img/output-screenshot.png)
