<h2>Decision Tree</h2>
<p>Graphical representation of all the possible solutions to a decisions based on given conditions</p>
<h3>Intro</h3>
<ul>
  <li>It starts with the root node that represents the entire undivided data population.</li>
  <li>The root node branches off to a number of solutions based on the condition.</li>
  <li>Decision tree keeps on growing with increasing number of decisions and conditions.</li>
  <li>We need to quantify how much a question reduces the uncertainity using a information gain concept - selecting the best question to ask at each point.</li>
  <li>Recursively building the tree on each of the new node continuing diving the data untile there are no further questions to ask reaching a leaf node.</li>
  <li>Questions need to be related to the nature of the dataset.</li>
</ul>

<h3>Demo</h3>
<ul>
  <li>When new sample comes in, then we start from the root node traversing tree untill the leaf node where we can assigne a label.</li>
  <li>Based on the features of the sample we can define the labels, f.e. 1 or 0.</li>
  <li>On every split step we need to come up with <b>the best split value (when text feature)</b> or <b>the best split value</b> (when numeric feature).</li>
  <li></li>
</ul>
