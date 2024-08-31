ground_truth_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

string_demo = f"The numbers on the image are only for easy differentiation and do not affect a person's social status. \
For each mark in this image it represents a person. \
There are several people in the image, and each person is marked with a number: {ground_truth_ids}. \
Judge each mark what he is doing, talking or queuing or other social status. Return in forms of 'mark:status'. \
The mark must be a number and the status must be talking, queuing, walking or photographing. Then group the mark. \
People who engage in an activity together should be in the same group. For example, taking photos and posing are considered a group. \
Return in forms of 'group:mark'. The mark and group must be a number. For example, you can return '''25:walking, 23:standing, 24:standing\n\ngroup1:23,24\ngroup2:25'''"

print(string_demo)
