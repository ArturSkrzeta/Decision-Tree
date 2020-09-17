<h2>Decision Tree</h2>
<p>Graphical representation of all the possible solutions to a decisions based on given conditions</p>
<h3>Intro</h3>
<ul>
  <li>It starts with the root node that represents the entire undivided data labels.</li>
  <li>The root node branches off to a number of solutions based on a sample features condition.</li>
  <li>Decision tree keeps on growing with increasing number of decisions and conditions.</li>
  <li>We need to quantify how much a question reduces the uncertainity uusing the information gain concept - selecting the best question to ask at each point.</li>
  <li>Recursively building the tree on each of the new node continuing diving the data untill there are no further questions to ask reaching a leaf node.</li>
  <li>Questions need to be related to the nature of the dataset.</li>
</ul>

<h3>Training Model</h3>
<ul>
  <li>Greedy search looping over all possible features and all possible threasholds of actual sampales.</li>
  <li>Calculation:
    <br>
    - <b>Entropy calculation</b> - measure of uncertainity for finding best split.<br>
    - <b>Infomation gain</b> - measure of how much informaction child node gets from the split.<br>
  </li>
  <li>Saving the best split based on the best information gain at each node.</li>
  <li>While building the tree we need to apply some stopping criteria to prevent tree from growing any further:
    <br>
    - max depth,<br>
    - min samples at a node,<br>
    - only one class left at a node,<br>
  </li>
  <li>When leaf node reached, we take the most common class label at the node.</li>
</ul>

<h3>Label prediction for a new sample</h3>
<ul>
  <li>Traversing tree recursively.</li>
  <li>During recursion, it takes a look at the node's best split feature aginst a new sample feature.</li>
  <li>Moving on to left or right node depending on the test condition for a new sample feature.</li>
</ul>

<h3>Demo</h3>
<ul>
  <li>When new sample comes in, then we start from the root node traversing tree untill the leaf node where we can assign a label.</li>
  <li>Based on the features of the sample we can define the labels, f.e. 1 or 0.</li>
  <li>On every split step we need to come up with <b>the best split value (when text feature)</b> or <b>the best split threshold</b> (when numeric feature).</li>
</ul>


<h2>Math with Numpy</h2>
<h3>numpy.bincounter</h3>
<ul>
  <li>Counts number of occurences of each value in non-negative ints array.</li>
  <li>The number of bins is one larger than the largest value in an input array.</li>
  <li>Each bin gives the number of occurrences of its index value in x</li>
  <br>
  <img src="images/bincounter.JPG">
</ul>
