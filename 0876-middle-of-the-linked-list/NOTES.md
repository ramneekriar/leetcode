<h2><a href="https://leetcode.com/problems/middle-of-the-linked-list/">876. Middle of the Linked List</a></h2><h3>Easy</h3>

<p>We want to return the middle of the linked list. If there are two middle nodes, we want to return the second middle node. Intialize a dummy node and point it to head. Create a slow and fast pointer and point it to dummy as well. While fast.next and fast.next.next exist (so there are still two nodes after our current fast), increment slow by 1 and increment fast by 2. At the end of the loop, return slow.next.</p>
