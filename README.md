# PMGsorter
Are you tired of sorting **big** excel sheets to try to please as many people as possible, on choices they made ? If yes, then this is for you.

## Description of the problem

Let $n$ be the number of subjects, we have $m$ activities with $p_j$ places each( $j \in [1..m]$ ). We want to give $k$ activities to each of the subject. Each subject classifies the activities based on his preferences. The goal is to satisfy the subjects at best considering their classification of the activities.

### Equations

In order to deal with this problem, we start by defining :
$$A = (a_{i,j}) \in \\{0,1\\}^{[1..n]\times[1..m]}$$
the matrix of choices; if $a_{i,j} = 1$ that means that the subject $i$ was given the activity $j$.

We also define :
$$W = (w_{i,j}) \in \mathbb{R_+}^{[1..n]\times[1..m]}$$
the matrix of preferences (or weight matrix); if $w_{i,j}$ is higher that means that the subject $i$ wants the activity $j$ more.

Finally, we have :
$$P^T = (p_{i,j}) \in \mathbb{N^*_+}^{[1..m]}$$
were $p_j$ is the number of places in the activity $j$.

#### Preliminary verifications

We start by checking that :
$$\sum_{j=1}^{m}{p_j} \geq n\times k$$
which just means that there are enough places overall for everyone.

#### What we want

We want to satisfy as much as possible the subjects in their choices :
$$\max \sum_{i,j}{a_{i,j}w_{i,j}}$$

#### Necessary constraints

Those are the constraints inherent to the problem : <br /> <br />
each subject has exactly k activites
$$\forall i \in [1..n], \sum_{j=1}^{m}{a_{i,j}} = k$$

not more subject by activity than the maximum number allowed
$$\forall j \in [1..m], \sum_{i=1}^{n}{a_{i,j}} \le p_j$$

#### Additional constraints

As it is now, we could end up in a configuration where some people have all they want, and some other get all their bad choices. Since we don't want that, we introduce several sets of constraints. Some of those may yield good results in some configurations, but may make it impossible to solve the problem in other configurations. <br /> This why we let the sorter test different constraints, from stronger to weaker until it finds a configuration in which it works.
<br /> <br />
Here are the constraints, from stronger to weaker : <br />
**Work in progress**

#### Choice of the scores for preferences
The subjects can classify the activities from $1^{st}$ to $k^{th}$, we then attribute a score based on the classification, with a predetermined law. <br />
We choose to use a modified exponential law (which will give a high score to the first choices, and a low score to the last choices). We thus have :
$$w_{i,j} = V_{max} e^{-(k_{i,j}-1)\times\lambda}$$
where $k_{i,j}$ is the classification of the activity $j$ by the subject $i$, $V_{max}$ is the value given to the $1^{st}$ choice, $\lambda$ is the decrease speed.

#### Notion of time and activity repartition
**Work in progress**
