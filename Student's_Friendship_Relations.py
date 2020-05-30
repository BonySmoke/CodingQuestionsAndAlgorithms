'''
A classroom consists of N students, whose friendships can be represented in an adjacency list.
For example, the following descibes a situation
where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

friendship_dict = {
 0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3],
 }

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group.
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
'''
friendship_dict = {
 0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3],
 }

def create_group(friends_num, friendship_dict, group):
    group.add(friends_num)
    #adds all dictionary values of the selected friend
    nodes = friendship_dict[friends_num]
    if not nodes:
        return None

    #recuresively adds friends to a friend group
    for i in nodes:
        if i not in group:
            create_group(i, friendship_dict, group)

def find_groups(friends_num, friendship_dict, groups):
    n = len(friends_num)

    while n:
        #creates a new group for every new set of friends
        new_group = set()
        friend = list(friends_num)[0]
        create_group(friend, friendship_dict, new_group)
        groups.append(new_group)
        #delets the checked friend from the friendship_dict
        friends_num -= new_group
        n = len(friends_num)

    return groups

def friend_groups_num(friends_num, friendship_dict):
    groups = []
    alone = set()
    for friend in friends_num:
        #if a key doesn't have any values, it's an isolated group
        if not friendship_dict[friend]:
            alone.add(friend)
            groups.append(friend)

    for person in alone:
        #removes all the records about the added isolated person
        friends_num.remove(person)
        del friendship_dict[person]

    groups = find_groups(friends_num, friendship_dict, groups)
    print(groups)

    return f'There are {len(groups)} groups of friends'

print(friend_groups_num(set(range(1, 7)), friendship_dict))
