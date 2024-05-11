class Solution:

    def bigest_step(self, ran, lst):
        """
        Returns a list of tuples (containing the index, and the value) filtered by the size of the members, 
        starting from the smallest member and adding every member that is larger than the previous member.

        Parameters:
        ran (int): Gets a starting point of index.
        lst (list): A list of integers.

        Returns:
        list of tuples: A list of tuples, each containing the index and the value.

        Note:
        - The index direction is determined by the starting point (ran). If ran is not 0, the index direction is reversed.
        - The function iterates over the list, adding tuples to the result list whenever a member is larger than the previous member.
        """
        order = True
        # check index direction
        if ran!= 0:
            order = False

        previeos = 0
        steps = []
        for i in range(len(lst)):
            node = lst[i]
            if node > previeos:
                steps += [(ran, node)]
                previeos = node
            if order:   
                ran += 1
            else:
                ran -= 1
        return steps

    def maxArea(self, lst):
        """
        Calculates the maximum area of a rectangle that can be formed by a subset of consecutive elements in a list.

        Parameters:
        lst (list): A list of integers.

        Returns:
        str: A string indicating the maximum area and the corresponding indices.

        Note:
        - The function first filters the relevant values from both ends of the list using the `bigest_step` method.
        - It then iterates over the filtered values from both ends, calculating the area of each possible rectangle.
        - The function keeps track of the maximum area and the corresponding indices.
        - Finally, it returns a string indicating the maximum area and the corresponding indices.
        """
        # Filters the relevant values from right
        steps_pre = self.bigest_step(0, lst=lst)
        bigest = steps_pre[-1][1]
        # index of the bigest from the end to the beginning
        last_node_index = (len(lst) - steps_pre[-1][0]+1) * -1
        # Filters the relevant values from right
        other_side = self.bigest_step(len(lst)-1, lst[-1:last_node_index:-1])

        sum = 0
        pre_r= 0
        pre_l = 0
        
        curent_left, curent_right = (0, 0), (0, 0)

        while True:
            curent_right = steps_pre[pre_r]
            curent_left = other_side[pre_l]
            smallest = min(curent_right[1], curent_left[1])
            multi = smallest * (curent_left[0] - curent_right[0])
            if multi > sum:
                sum = multi
                ind = (curent_right[0], curent_left[0])

            if curent_right[1] == smallest:
                pre_r += 1

            if curent_left[1] == smallest:
                pre_l += 1#
            
            if curent_left[1] == bigest and curent_right[1] == bigest:
                break

        return (f"total sum is: {sum}. between index {ind[0]} to index {ind[1]}")

k = Solution()
def check_sum(lst1, o=k):
        return k.maxArea(lst1)

