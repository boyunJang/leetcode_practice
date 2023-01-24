class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_dic = collections.defaultdict(list)
        left_course = collections.defaultdict(int)
        for pre, aft in prerequisites:
            pre_dic[pre].append(aft)
            left_course[aft] += 1

        avail_course = [i for i in range(numCourses) if i not in left_course]
        taken_course = 0
        while len(avail_course) > 0:
            course = avail_course.pop(0)
            taken_course += 1
            if taken_course == numCourses: return True
            for new_course in pre_dic[course]:
                left_course[new_course] -= 1
                if left_course[new_course] == 0:
                    avail_course.append(new_course)
        return False