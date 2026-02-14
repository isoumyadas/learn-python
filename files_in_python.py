git_commit_md_file = open("git_commits.md")
print(git_commit_md_file.read()) # read content of file
# When you print above print statement three times, it will only print one time. Why? because it uses cursor, once cursor is at end of the line it ends, for what you can use:

git_commit_md_file.seek(0)
print(git_commit_md_file.read())
git_commit_md_file.seek(0)
# for print only one line on the file:
print(git_commit_md_file.readline())
git_commit_md_file.seek(0)
#  for printing all the content in file in the list
print(git_commit_md_file.readlines())

# To close the file
print(git_commit_md_file.close())

print("*" * 30)
# Proper way to work with files: 

# Here we don't need to close the file, their is mode where we can read,write the file. And read is by default.
"""
r => read
w => write
r+ => read & write
"""
with open("git_commits.md", mode="r") as my_file:
    # text_file = my_file.write() # this will overwrite the file you have in your file.
    # print(text_file)
    print(my_file.readlines())


# write the file
with open("git_commits.md", mode="r") as my_file:
    # text_file = my_file.write() # this will overwrite the file you have in your file.
    # print(text_file)
    pass

