# Data Objects, Types, and Visualization

Data sets are collections of data that are made up of objects or is a file that contains one or more records. A data object represents an entity. For instance, in a university possible entities could include students, professors, and courses. Data objects are typically describe by attributes. Data objects can also be referred to as samples, examples, instances, data points, or objects. More precisely, if the data are stored in a database, they are called data tuples; that is, the rows of a database corresponds to the data objects and the columns corresponds to attributes.

## Attribute

An attribute is a data field, representing a characteristic or feature of a data object. It's also referred to as a dimension. In data warehousing, attribute refres to a dimension, in machine learning it is often called a feature, and in statistics it's called a variable.

Attributes describing a customer may include an ID, address, name, and so on. A set of attributes used to describe a given object is called an attribute vector or feature vector. The distribution of data involving one attribute or variable is called univariate. A bivariate distribution involves two attributs and so on.

The type of an attribute is determined by the set of possible values - nominal, binary, ordinal, or numeric - the attribute can have. In databases, it is said that data objects should have values, for a particular attribute, that belong to its domain. For instance, integers cannot store string values.

### Nominal Attribute

Nominal means "relating to names". The values of nominal attributes are symbols or names of things. Each value represents some kind of category, code, or state and so nominal attributes are also called categorical attributes. The values do not have a meaningful order. In computer science, the values are also known as enumerations.

To drive the point home, let's make an example. Suppose that hair_color and marital status are two attributes describing a person. Possible values for hair_color are black, brown, red, auburn, gray, and white. The attribute marital status can take the values single, married, divorced, widowed.

Although nominal attributes are represented as codes, state, and categories, it is possible to represent such symbols with numbers. This is called encoding. For instance, we can use the code 0 for black, 1 for white, 2 for brown and so on in the attribute hair colour. However, in such cases the numbers are not inteded to be used quantitatively. That is, mathematical operations on values of nominal attributes do not make any sense and are meaningless. For example, imagine adding together a code for black with another code for gray hair. "What is the result of that?"

Because nominal attribute do not have any meaningful order about them and are not quantitative, it makes no sense to find the mean (average) value or median (middle) value for such an attribute, given a set of objects. One thing that is of interest, however, is the attribute's most commonly occuring value. This value known as the mode, is one measure of central tendency.

### Binary Attributes

A binary attribute is a nominal attribute with only two categories or states; 0 or 1 where 0 typically means tha the attributes is absent while 1 means that it is present. Binary attributes are referred to as Boolean if the two states correspond to true and false.

For example, given the attribute smoker describing a patient object, 1 indicates that the patient smokes while 0 represents that he/she does not.

A binary attribute is symmetric if both states are equally valuable and carry the same weight; that is, there is no preference on which outcome should be coded as 0 or 1. One such example could be gender have the states male and female.

On the contrary, a binary attribute is asymmetric if the outcome of the states are not equally important such as the negative and positive outcomes of a medical test for autism. By convention, we code the most important outcome, which is usually the rarest one, by 0 and the other by 0. For instance, in an HIV medical test, 1 could mean positive and 0 representing a negative status.

### Ordinal Attributes

An ordinal attribute is one with possible values that have a meaningful order or ranking among them, but the magnitude between sucessive values is not known. As an example, think of the size of T-shirts. This nominal attribute has 3 possible value which are: small, medium, and large. The values have a meaningful order or sequence (which corresponds to increasing drink size); however, we cannot tell from the values how much bigger medium is to small. Other examples could include grades in a university; we cannot quantify the differnce between A+ and A.

Ordinal attributes are useful for registering subjective assessments of qualities that cannot be measures objectively; thus ordinal attributes are often used in surverys for rating. In one survery, participants were asked to rate how satisfied they were as customers. Customer statisfaction had the following categories: 0: very dissatisfied, 1: somewhat dissatisfied, 2: neutral, 4: very satisfied.

Ordinal attributs may also obtain from discretization of numeric quantities by splitting the value into a finite range of ordered categories. For instance, given an attribute family_size which has values rangin from 2 to 15 we could discretize them into the bins: small family, medium, extended family.

The central tendency of ordingal attribute can be represented by its mode and its median but the mean cannot be defined.

Note tha nominal, binary, and ordinal attributes are qualitative. That is, they describe a feature of an object without giving an actual size or quantity. The values of such qualitative attributes are typically words representing categories. If integers are ever used, they represent the catogories. For instance, in a machine learning task, you can encode a nominal attribute because the model works well with numbers.

### Numeric Attributes

A numeric attribute is quantitative; that is, it is a measurable quantity represented in integer or real values. Numeric attributes can be interval-scaled or ratio-scaled.

Interval scaleed attributes are measures on a scale of equal-size units. The values of interval-scaled attributes have no order and can be positive, zero, or negative. Thus, in addition to providing a ranking of values, such attributs allow us to compare and quantify the diffrence between values. For exaple, temperature is an interval-scaled attribute. Say we have 20 ℃ and 15 ℃ we can say that 20 is five degress higher than 15 and these could be ranked either in increasing or decreasing order. Because interval-scaled attributes are numerics, can compute their mean value in additon to the median and mode measures of central tendency.

A ratio-scaled attribute is a numerical attribute with an inherent zero-point. That is, if a measurement is ratio-scaled, we can speak of a value as being a multiple (or ratio) of another value. In addition, the values are ordered and we can also compute the difference between values, as welll as the mean, mode, and median. For example, the attribute years_of_experience is ratio-scaled since we have 0 years of experience as the zero-point.

## Discrete and Continous Attributs

A discrete attribute has a finite or countably infinite set of values, which may or may not be represented as integers. The attributes hair_color, smoker, drink_size, or medical_test each have a finite number of values or observations and so are discrete.

An attribute is countably infinite if the set of possible values is infinite but the values can be put in a one-to-one correspondence with natural numbers. For example, the attribute customer_ID is countably infinite. The number of customers can grow infinity, but in reality, the actual set of values is countable.

If an attribute is not discrete, it is continous. Numeric and continous attribute can be used interchangably. Continuous values are real numbers, which numeric values can either be integers or real numbers (one category is a subset of the other). In practice, real values are represented using infinite number of digits. Continous attributes are typically represented using as floating point variables.
