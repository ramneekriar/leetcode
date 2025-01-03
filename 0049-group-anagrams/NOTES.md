<h2><a href="https://leetcode.com/problems/group-anagrams/description/">49. Group Anagrams</a></h2><h3>Easy</h3>

<p>Create a hashmap with a defaultdict with a default value of a list. Iterate over the given strings, and sort each one. That sorted value will be our key. Append the string as normal into that sorted key in our hashmap. At the end, return the values of the hashmap as a list.</p>