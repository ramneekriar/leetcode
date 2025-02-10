<h2><a href="https://leetcode.com/problems/single-number/description/">135. Single Number</a></h2><h3>Easy</h3>

<p>We are going to be using XOR for to determine which number only appears once. The idea is that the number represented in binary will cancel each other out when XORd, so the number that does not exist in a pair will be the one that remains.</p>

<p>XOR</p>
<li>0 XOR 0 = 0</li>
<li>0 XOR 1 = 1</li>
<li>1 XOR 0 = 1</li>
<li>1 XOR 1 = 0</li>
