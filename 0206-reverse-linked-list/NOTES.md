<h2><a href="https://leetcode.com/problems/reverse-linked-list/">206. Reverse Linked List</a></h2><h3>Easy</h3>

<p>This is a recursive problem. First check if head does not exist, then simply return None. Store the current value of head in a pointer called newHead. Then check if the node after head exists, if it does we want to call our function again with the head.next value and store that into a local pointer called newHead. What we are doing here is essentially going down the entire linkedList until the very end, until head.next points to None. In this case, the loop is not entered and newHead points to the very last known value.</p>

<p>1 -> 2 -> 3 -> 4 -> 5 -> None</p>

<p>Let's work with this linked list as an example. Our pointer newHead points to 5 in this case, and now outside the loop we set head.next to None (so 5 -> None) and return the value of newHead. newHead right now would points to (5 -> None).</p>

<p>As we work back up the recursion call stack, we have to continue with the rest of the code in the if block. The next line in the if block is setting head.next.next = head. This is taking whatever value is at head in the call stack, and putting it after the value of newHead.</p>

<p>Keep in mind head points to 4 and newHead points to 5. So this is what we have so far:</p>
<p>1 -> 2 -> 3 -> 4 -> 5 -> None </p>
<p>____________|____|______<p>
<p>.................head...newHead</p>

<p>So now, head.next.next = head essentially puts 4 after 5 since 4 still has a reference to 5 in the linked list. And now outside of the if statement, 4 still refers to the head pointer, so head.next = None results in 5 -> 4 -> None. Then we return newHead, which kept a reference to the head, as in 4 so that we are able to build upon this reversed linked list from this point. This is then repeated back up the recursion call stack.</p>

<p><strong>Even though we start reversing the list from the back onwards and work our way up through recursion, the head value at that current moment in the call stack will always have a reference/points next to the last element of the reversed linked list. This is why we are able to use head.next.next to put it in its reversed position.</p>