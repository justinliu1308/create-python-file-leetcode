import requests
import os
from bs4 import BeautifulSoup

##################################################################################################
# Paste the full link of each problem you wish to create a file for, with or with '/description/'
link = 'https://leetcode.com/problems/same-tree/'
##################################################################################################

def main(link):
    def api_query(link):
        # Format problem name for query and obtain structured filename for local file creation

        # Extract problem name (ex: find-the-town-judge) from URL for query
        split_link = link.split('/')
        problem_name = split_link[4]

        # Query for leetcode.com/graphql
        data = {"operationName":"questionData","variables":{"titleSlug":problem_name},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
        r = requests.post('https://leetcode.com/graphql', json = data).json()
        soup = BeautifulSoup(r['data']['question']['content'], 'lxml')

        # Extract problem title, level of difficulty, and question prompt from query
        number = r['data']['question']['questionFrontendId']
        title = r['data']['question']['title'].title() + '.py'
        filename = number + ' ' + title
        difficulty = r['data']['question']['difficulty']
        question =  soup.get_text().replace('\n',' ')
        question = question.split('Example')[0]
        
        return filename, difficulty, question

    def check_file_exists(filename):
        # Check if filename already exists, and if yes, do nothing to prevent file overwrite and data loss
        if filename in os.listdir():
            return True
        else:
            return False

    def create_local_file(filename, link, difficulty, question):
        # Create a LeetCode problem local Python file
        if 'description' in link: link = link[:-12]     # https:// ...problem-name/description/ isn't necessary, just ..problem-name/ is sufficient
        new_file = open(filename, 'w')
        new_file.write('# ' + link + '\n# ' + difficulty + '\n\n# ' + question + '\n\n# Your code:\n\n')
        new_file.close()

    filename, difficulty, question = api_query(link)
    exist = check_file_exists(filename)
    if exist == True:
        print("File already exists. Nothing was done in order to prevent file overwrite.\nOpening existing file...")
    else:
        create_local_file(filename, link, difficulty, question)
        print("New file created:", filename, "\nOpening new file...")

    # Open the file in new tab
    os.startfile(filename)

if __name__ == "__main__":
    main(link)

