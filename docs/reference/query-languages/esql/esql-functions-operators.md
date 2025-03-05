---
navigation_title: "Functions and operators"
---

# {{esql}} functions and operators [esql-functions-operators]


{{esql}} provides a comprehensive set of functions and operators for working with data. The reference documentation is divided into the following categories:

## Functions overview [esql-functions]

::::{dropdown} **Aggregate functions**
* [`AVG`](esql-functions-operators.md#esql-avg)
* [`COUNT`](esql-functions-operators.md#esql-count)
* [`COUNT_DISTINCT`](esql-functions-operators.md#esql-count_distinct)
* [`MAX`](esql-functions-operators.md#esql-max)
* [`MEDIAN`](esql-functions-operators.md#esql-median)
* [`MEDIAN_ABSOLUTE_DEVIATION`](esql-functions-operators.md#esql-median_absolute_deviation)
* [`MIN`](esql-functions-operators.md#esql-min)
* [`PERCENTILE`](esql-functions-operators.md#esql-percentile)
* [preview] [`ST_CENTROID_AGG`](esql-functions-operators.md#esql-st_centroid_agg)
* [preview] [`ST_EXTENT_AGG`](esql-functions-operators.md#esql-st_extent_agg)
* [`STD_DEV`](esql-functions-operators.md#esql-std_dev)
* [`SUM`](esql-functions-operators.md#esql-sum)
* [`TOP`](esql-functions-operators.md#esql-top)
* [`VALUES`](esql-functions-operators.md#esql-values)
* [`WEIGHTED_AVG`](esql-functions-operators.md#esql-weighted_avg)

::::


::::{dropdown} **Grouping functions**
* [`BUCKET`](esql-functions-operators.md#esql-bucket)
* [preview] [`CATEGORIZE`](esql-functions-operators.md#esql-categorize)

::::


::::{dropdown} **Conditional functions and expressions**
* [`CASE`](esql-functions-operators.md#esql-case)
* [`COALESCE`](esql-functions-operators.md#esql-coalesce)
* [`GREATEST`](esql-functions-operators.md#esql-greatest)
* [`LEAST`](esql-functions-operators.md#esql-least)

::::


%  <Type-specific functions alphabetically ordered>

::::{dropdown} **Date and time functions**
* [`DATE_DIFF`](esql-functions-operators.md#esql-date_diff)
* [`DATE_EXTRACT`](esql-functions-operators.md#esql-date_extract)
* [`DATE_FORMAT`](esql-functions-operators.md#esql-date_format)
* [`DATE_PARSE`](esql-functions-operators.md#esql-date_parse)
* [`DATE_TRUNC`](esql-functions-operators.md#esql-date_trunc)
* [`NOW`](esql-functions-operators.md#esql-now)

::::


::::{dropdown} **IP functions**
* [`CIDR_MATCH`](esql-functions-operators.md#esql-cidr_match)
* [`IP_PREFIX`](esql-functions-operators.md#esql-ip_prefix)

::::


::::{dropdown} **Math functions**
* [`ABS`](esql-functions-operators.md#esql-abs)
* [`ACOS`](esql-functions-operators.md#esql-acos)
* [`ASIN`](esql-functions-operators.md#esql-asin)
* [`ATAN`](esql-functions-operators.md#esql-atan)
* [`ATAN2`](esql-functions-operators.md#esql-atan2)
* [`CBRT`](esql-functions-operators.md#esql-cbrt)
* [`CEIL`](esql-functions-operators.md#esql-ceil)
* [`COS`](esql-functions-operators.md#esql-cos)
* [`COSH`](esql-functions-operators.md#esql-cosh)
* [`E`](esql-functions-operators.md#esql-e)
* [`EXP`](esql-functions-operators.md#esql-exp)
* [`FLOOR`](esql-functions-operators.md#esql-floor)
* [`HYPOT`](esql-functions-operators.md#esql-hypot)
* [`LOG`](esql-functions-operators.md#esql-log)
* [`LOG10`](esql-functions-operators.md#esql-log10)
* [`PI`](esql-functions-operators.md#esql-pi)
* [`POW`](esql-functions-operators.md#esql-pow)
* [`ROUND`](esql-functions-operators.md#esql-round)
* [`SIGNUM`](esql-functions-operators.md#esql-signum)
* [`SIN`](esql-functions-operators.md#esql-sin)
* [`SINH`](esql-functions-operators.md#esql-sinh)
* [`SQRT`](esql-functions-operators.md#esql-sqrt)
* [`TAN`](esql-functions-operators.md#esql-tan)
* [`TANH`](esql-functions-operators.md#esql-tanh)
* [`TAU`](esql-functions-operators.md#esql-tau)

::::


::::{dropdown} **Search functions**
* [preview] [`KQL`](esql-functions-operators.md#esql-kql)
* [preview] [`MATCH`](esql-functions-operators.md#esql-match)
* [preview] [`QSTR`](esql-functions-operators.md#esql-qstr)

::::


::::{dropdown} **Spatial functions**
* [`ST_DISTANCE`](esql-functions-operators.md#esql-st_distance)
* [`ST_INTERSECTS`](esql-functions-operators.md#esql-st_intersects)
* [`ST_DISJOINT`](esql-functions-operators.md#esql-st_disjoint)
* [`ST_CONTAINS`](esql-functions-operators.md#esql-st_contains)
* [`ST_WITHIN`](esql-functions-operators.md#esql-st_within)
* [`ST_X`](esql-functions-operators.md#esql-st_x)
* [`ST_Y`](esql-functions-operators.md#esql-st_y)
* [preview] [`ST_ENVELOPE`](esql-functions-operators.md#esql-st_envelope)
* [preview] [`ST_XMAX`](esql-functions-operators.md#esql-st_xmax)
* [preview] [`ST_XMIN`](esql-functions-operators.md#esql-st_xmin)
* [preview] [`ST_YMAX`](esql-functions-operators.md#esql-st_ymax)
* [preview] [`ST_YMIN`](esql-functions-operators.md#esql-st_ymin)

::::


::::{dropdown} **String functions**
* [`BIT_LENGTH`](esql-functions-operators.md#esql-bit_length)
* [`BYTE_LENGTH`](esql-functions-operators.md#esql-byte_length)
* [`CONCAT`](esql-functions-operators.md#esql-concat)
* [`ENDS_WITH`](esql-functions-operators.md#esql-ends_with)
* [`FROM_BASE64`](esql-functions-operators.md#esql-from_base64)
* [`HASH`](esql-functions-operators.md#esql-hash)
* [`LEFT`](esql-functions-operators.md#esql-left)
* [`LENGTH`](esql-functions-operators.md#esql-length)
* [`LOCATE`](esql-functions-operators.md#esql-locate)
* [`LTRIM`](esql-functions-operators.md#esql-ltrim)
* [`MD5`](esql-functions-operators.md#esql-md5)
* [`REPEAT`](esql-functions-operators.md#esql-repeat)
* [`REPLACE`](esql-functions-operators.md#esql-replace)
* [`REVERSE`](esql-functions-operators.md#esql-reverse)
* [`RIGHT`](esql-functions-operators.md#esql-right)
* [`RTRIM`](esql-functions-operators.md#esql-rtrim)
* [`SHA1`](esql-functions-operators.md#esql-sha1)
* [`SHA256`](esql-functions-operators.md#esql-sha256)
* [`SPACE`](esql-functions-operators.md#esql-space)
* [`SPLIT`](esql-functions-operators.md#esql-split)
* [`STARTS_WITH`](esql-functions-operators.md#esql-starts_with)
* [`SUBSTRING`](esql-functions-operators.md#esql-substring)
* [`TO_BASE64`](esql-functions-operators.md#esql-to_base64)
* [`TO_LOWER`](esql-functions-operators.md#esql-to_lower)
* [`TO_UPPER`](esql-functions-operators.md#esql-to_upper)
* [`TRIM`](esql-functions-operators.md#esql-trim)

::::


%  </Type-specific functions alphabetically ordered>

::::{dropdown} **Type conversion functions**
* [`TO_BOOLEAN`](esql-functions-operators.md#esql-to_boolean)
* [`TO_CARTESIANPOINT`](esql-functions-operators.md#esql-to_cartesianpoint)
* [`TO_CARTESIANSHAPE`](esql-functions-operators.md#esql-to_cartesianshape)
* [preview] [`TO_DATEPERIOD`](esql-functions-operators.md#esql-to_dateperiod)
* [`TO_DATETIME`](esql-functions-operators.md#esql-to_datetime)
* [`TO_DATE_NANOS`](esql-functions-operators.md#esql-to_date_nanos)
* [`TO_DEGREES`](esql-functions-operators.md#esql-to_degrees)
* [`TO_DOUBLE`](esql-functions-operators.md#esql-to_double)
* [`TO_GEOPOINT`](esql-functions-operators.md#esql-to_geopoint)
* [`TO_GEOSHAPE`](esql-functions-operators.md#esql-to_geoshape)
* [`TO_INTEGER`](esql-functions-operators.md#esql-to_integer)
* [`TO_IP`](esql-functions-operators.md#esql-to_ip)
* [`TO_LONG`](esql-functions-operators.md#esql-to_long)
* [`TO_RADIANS`](esql-functions-operators.md#esql-to_radians)
* [`TO_STRING`](esql-functions-operators.md#esql-to_string)
* [preview] [`TO_TIMEDURATION`](esql-functions-operators.md#esql-to_timeduration)
* [preview] [`TO_UNSIGNED_LONG`](esql-functions-operators.md#esql-to_unsigned_long)
* [`TO_VERSION`](esql-functions-operators.md#esql-to_version)

::::


::::{dropdown} **Multi value functions**
* [`MV_APPEND`](esql-functions-operators.md#esql-mv_append)
* [`MV_AVG`](esql-functions-operators.md#esql-mv_avg)
* [`MV_CONCAT`](esql-functions-operators.md#esql-mv_concat)
* [`MV_COUNT`](esql-functions-operators.md#esql-mv_count)
* [`MV_DEDUPE`](esql-functions-operators.md#esql-mv_dedupe)
* [`MV_FIRST`](esql-functions-operators.md#esql-mv_first)
* [`MV_LAST`](esql-functions-operators.md#esql-mv_last)
* [`MV_MAX`](esql-functions-operators.md#esql-mv_max)
* [`MV_MEDIAN`](esql-functions-operators.md#esql-mv_median)
* [`MV_MEDIAN_ABSOLUTE_DEVIATION`](esql-functions-operators.md#esql-mv_median_absolute_deviation)
* [`MV_MIN`](esql-functions-operators.md#esql-mv_min)
* [`MV_PERCENTILE`](esql-functions-operators.md#esql-mv_percentile)
* [`MV_PSERIES_WEIGHTED_SUM`](esql-functions-operators.md#esql-mv_pseries_weighted_sum)
* [`MV_SORT`](esql-functions-operators.md#esql-mv_sort)
* [`MV_SLICE`](esql-functions-operators.md#esql-mv_slice)
* [`MV_SUM`](esql-functions-operators.md#esql-mv_sum)
* [`MV_ZIP`](esql-functions-operators.md#esql-mv_zip)

::::



## Operators overview [esql-operators-overview]

::::{dropdown} **Operators**
* [Binary operators](esql-functions-operators.md#esql-binary-operators)
* [Unary operators](esql-functions-operators.md#esql-unary-operators)
* [Logical operators](esql-functions-operators.md#esql-logical-operators)
* [`IS NULL` and `IS NOT NULL` predicates](esql-functions-operators.md#esql-predicates)
* [`Cast (::)`](esql-functions-operators.md#esql-cast-operator)
* [`IN`](esql-functions-operators.md#esql-in-operator)
* [`LIKE`](esql-functions-operators.md#esql-like-operator)
* [`RLIKE`](esql-functions-operators.md#esql-rlike-operator)
* [preview] [Search operators](esql-functions-operators.md#esql-search-operators)

::::



## {{esql}} aggregate functions [esql-agg-functions]


The [`STATS`](esql-commands.md#esql-stats-by) command supports these aggregate functions:

%  tag::agg_list[]

* [`AVG`](esql-functions-operators.md#esql-avg)
* [`COUNT`](esql-functions-operators.md#esql-count)
* [`COUNT_DISTINCT`](esql-functions-operators.md#esql-count_distinct)
* [`MAX`](esql-functions-operators.md#esql-max)
* [`MEDIAN`](esql-functions-operators.md#esql-median)
* [`MEDIAN_ABSOLUTE_DEVIATION`](esql-functions-operators.md#esql-median_absolute_deviation)
* [`MIN`](esql-functions-operators.md#esql-min)
* [`PERCENTILE`](esql-functions-operators.md#esql-percentile)
* [preview] [`ST_CENTROID_AGG`](esql-functions-operators.md#esql-st_centroid_agg)
* [preview] [`ST_EXTENT_AGG`](esql-functions-operators.md#esql-st_extent_agg)
* [`STD_DEV`](esql-functions-operators.md#esql-std_dev)
* [`SUM`](esql-functions-operators.md#esql-sum)
* [`TOP`](esql-functions-operators.md#esql-top)
* [`VALUES`](esql-functions-operators.md#esql-values)
* [`WEIGHTED_AVG`](esql-functions-operators.md#esql-weighted_avg)

%  end::agg_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `AVG` [esql-avg] 

**Syntax**

:::{image} images/avg.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

The average of a numeric field.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS AVG(height)
```

| AVG(height):double |
| --- |
| 1.7682 |

The expression can use inline functions. For example, to calculate the average over a multivalued column, first use `MV_AVG` to average the multiple values per row, and use the result with the `AVG` function

```esql
FROM employees
| STATS avg_salary_change = ROUND(AVG(MV_AVG(salary_change)), 10)
```

| avg_salary_change:double |
| --- |
| 1.3904535865 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `COUNT` [esql-count] 

**Syntax**

:::{image} images/count.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Expression that outputs values to be counted. If omitted, equivalent to `COUNT(*)` (the number of rows).

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the total number (count) of input values.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | long |
| cartesian_point | long |
| date | long |
| double | long |
| geo_point | long |
| integer | long |
| ip | long |
| keyword | long |
| long | long |
| text | long |
| unsigned_long | long |
| version | long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS COUNT(height)
```

| COUNT(height):long |
| --- |
| 100 |

To count the number of rows, use `COUNT()` or `COUNT(*)`

```esql
FROM employees
| STATS count = COUNT(*) BY languages
| SORT languages DESC
```

| count:long | languages:integer |
| --- | --- |
| 10 | null |
| 21 | 5 |
| 18 | 4 |
| 17 | 3 |
| 19 | 2 |
| 15 | 1 |

The expression can use inline functions. This example splits a string into multiple values using the `SPLIT` function and counts the values

```esql
ROW words="foo;bar;baz;qux;quux;foo"
| STATS word_count = COUNT(SPLIT(words, ";"))
```

| word_count:long |
| --- |
| 6 |

To count the number of times an expression returns `TRUE` use a [`WHERE`](esql-commands.md#esql-where) command to remove rows that shouldn’t be included

```esql
ROW n=1
| WHERE n < 0
| STATS COUNT(n)
```

| COUNT(n):long |
| --- |
| 0 |

To count the same stream of data based on two different expressions use the pattern `COUNT(<expression> OR NULL)`. This builds on the three-valued logic ({{wikipedia}}/Three-valued_logic[3VL]) of the language: `TRUE OR NULL` is `TRUE`, but `FALSE OR NULL` is `NULL`, plus the way COUNT handles `NULL`s: `COUNT(TRUE)` and `COUNT(FALSE)` are both 1, but `COUNT(NULL)` is 0.

```esql
ROW n=1
| STATS COUNT(n > 0 OR NULL), COUNT(n < 0 OR NULL)
```

| COUNT(n > 0 OR NULL):long | COUNT(n < 0 OR NULL):long |
| --- | --- |
| 1 | 0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `COUNT_DISTINCT` [esql-count_distinct] 

**Syntax**

:::{image} images/count_distinct.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Column or literal for which to count the number of distinct values.

`precision`
:   Precision threshold. Refer to [Counts are approximate](esql-functions-operators.md#esql-agg-count-distinct-approximate). The maximum supported value is 40000. Thresholds above this number will have the same effect as a threshold of 40000. The default value is 3000.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the approximate number of distinct values.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | precision | result |
| --- | --- | --- |
| boolean | integer | long |
| boolean | long | long |
| boolean | unsigned_long | long |
| boolean |  | long |
| date | integer | long |
| date | long | long |
| date | unsigned_long | long |
| date |  | long |
| date_nanos | integer | long |
| date_nanos | long | long |
| date_nanos | unsigned_long | long |
| date_nanos |  | long |
| double | integer | long |
| double | long | long |
| double | unsigned_long | long |
| double |  | long |
| integer | integer | long |
| integer | long | long |
| integer | unsigned_long | long |
| integer |  | long |
| ip | integer | long |
| ip | long | long |
| ip | unsigned_long | long |
| ip |  | long |
| keyword | integer | long |
| keyword | long | long |
| keyword | unsigned_long | long |
| keyword |  | long |
| long | integer | long |
| long | long | long |
| long | unsigned_long | long |
| long |  | long |
| text | integer | long |
| text | long | long |
| text | unsigned_long | long |
| text |  | long |
| version | integer | long |
| version | long | long |
| version | unsigned_long | long |
| version |  | long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM hosts
| STATS COUNT_DISTINCT(ip0), COUNT_DISTINCT(ip1)
```

| COUNT_DISTINCT(ip0):long | COUNT_DISTINCT(ip1):long |
| --- | --- |
| 7 | 8 |

With the optional second parameter to configure the precision threshold

```esql
FROM hosts
| STATS COUNT_DISTINCT(ip0, 80000), COUNT_DISTINCT(ip1, 5)
```

| COUNT_DISTINCT(ip0, 80000):long | COUNT_DISTINCT(ip1, 5):long |
| --- | --- |
| 7 | 9 |

The expression can use inline functions. This example splits a string into multiple values using the `SPLIT` function and counts the unique values

```esql
ROW words="foo;bar;baz;qux;quux;foo"
| STATS distinct_word_count = COUNT_DISTINCT(SPLIT(words, ";"))
```

| distinct_word_count:long |
| --- |
| 5 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


### Counts are approximate [esql-agg-count-distinct-approximate] 

Computing exact counts requires loading values into a set and returning its size. This doesn’t scale when working on high-cardinality sets and/or large values as the required memory usage and the need to communicate those per-shard sets between nodes would utilize too many resources of the cluster.

This `COUNT_DISTINCT` function is based on the [HyperLogLog++](https://static.googleusercontent.com/media/research.google.com/fr//pubs/archive/40671.pdf) algorithm, which counts based on the hashes of the values with some interesting properties:

* configurable precision, which decides on how to trade memory for accuracy,
* excellent accuracy on low-cardinality sets,
* fixed memory usage: no matter if there are tens or billions of unique values, memory usage only depends on the configured precision.

For a precision threshold of `c`, the implementation that we are using requires about `c * 8` bytes.

The following chart shows how the error varies before and after the threshold:

% To generate this chart use this gnuplot script:
% [source,gnuplot]
% -------
% #!/usr/bin/gnuplot
% reset
% set terminal png size 1000,400
% 
% set xlabel "Actual cardinality"
% set logscale x
% 
% set ylabel "Relative error (%)"
% set yrange [0:8]
% 
% set title "Cardinality error"
% set grid
% 
% set style data lines
% 
% plot "test.dat" using 1:2 title "threshold=100", \
% "" using 1:3 title "threshold=1000", \
% "" using 1:4 title "threshold=10000"
% #
% -------
% 
% and generate data in a *test.dat* file using the below Java code:
% 
% [source,java]
% -------
% private static double error(HyperLogLogPlusPlus h, long expected) {
%     double actual = h.cardinality(0);
%     return Math.abs(expected - actual) / expected;
% }
% 
% public static void main(String[] args) {
%     HyperLogLogPlusPlus h100 = new HyperLogLogPlusPlus(precisionFromThreshold(100), BigArrays.NON_RECYCLING_INSTANCE, 1);
%     HyperLogLogPlusPlus h1000 = new HyperLogLogPlusPlus(precisionFromThreshold(1000), BigArrays.NON_RECYCLING_INSTANCE, 1);
%     HyperLogLogPlusPlus h10000 = new HyperLogLogPlusPlus(precisionFromThreshold(10000), BigArrays.NON_RECYCLING_INSTANCE, 1);
% 
%     int next = 100;
%     int step = 10;
% 
%     for (int i = 1; i ⇐ 10000000; ++i) {
%         long h = BitMixer.mix64(i);
%         h100.collect(0, h);
%         h1000.collect(0, h);
%         h10000.collect(0, h);
% 
%         if (i == next) {
%             System.out.println(i + " " + error(h100, i)*100 + " " + error(h1000, i)*100 + " " + error(h10000, i)*100);
%             next += step;
%             if (next >= 100 * step) {
%                 step *= 10;
%             }
%         }
%     }
% }
% -------
% 

![cardinality error](images/cardinality_error.png "")

For all 3 thresholds, counts have been accurate up to the configured threshold. Although not guaranteed, this is likely to be the case. Accuracy in practice depends on the dataset in question. In general, most datasets show consistently good accuracy. Also note that even with a threshold as low as 100, the error remains very low (1-6% as seen in the above graph) even when counting millions of items.

The HyperLogLog++ algorithm depends on the leading zeros of hashed values, the exact distributions of hashes in a dataset can affect the accuracy of the cardinality.

The `COUNT_DISTINCT` function takes an optional second parameter to configure the precision threshold. The precision_threshold options allows to trade memory for accuracy, and defines a unique count below which counts are expected to be close to accurate. Above this value, counts might become a bit more fuzzy. The maximum supported value is 40000, thresholds above this number will have the same effect as a threshold of 40000. The default value is `3000`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MAX` [esql-max] 

**Syntax**

:::{image} images/max.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

The maximum value of a field.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| date | date |
| date_nanos | date_nanos |
| double | double |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS MAX(languages)
```

| MAX(languages):integer |
| --- |
| 5 |

The expression can use inline functions. For example, to calculate the maximum over an average of a multivalued column, use `MV_AVG` to first average the multiple values per row, and use the result with the `MAX` function

```esql
FROM employees
| STATS max_avg_salary_change = MAX(MV_AVG(salary_change))
```

| max_avg_salary_change:double |
| --- |
| 13.75 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MEDIAN` [esql-median] 

**Syntax**

:::{image} images/median.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

The value that is greater than half of all values and less than half of all values, also known as the 50% [`PERCENTILE`](esql-functions-operators.md#esql-percentile).

::::{note} 
Like [`PERCENTILE`](esql-functions-operators.md#esql-percentile), `MEDIAN` is [usually approximate](esql-functions-operators.md#esql-percentile-approximate).
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS MEDIAN(salary), PERCENTILE(salary, 50)
```

| MEDIAN(salary):double | PERCENTILE(salary, 50):double |
| --- | --- |
| 47003 | 47003 |

The expression can use inline functions. For example, to calculate the median of the maximum values of a multivalued column, first use `MV_MAX` to get the maximum value per row, and use the result with the `MEDIAN` function

```esql
FROM employees
| STATS median_max_salary_change = MEDIAN(MV_MAX(salary_change))
```

| median_max_salary_change:double |
| --- |
| 7.69 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

::::{warning} 
`MEDIAN` is also [non-deterministic](https://en.wikipedia.org/wiki/Nondeterministic_algorithm). This means you can get slightly different results using the same data.

::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MEDIAN_ABSOLUTE_DEVIATION` [esql-median_absolute_deviation] 

**Syntax**

:::{image} images/median_absolute_deviation.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

Returns the median absolute deviation, a measure of variability. It is a robust statistic, meaning that it is useful for describing data that may have outliers, or may not be normally distributed. For such data it can be more descriptive than standard deviation.  It is calculated as the median of each data point’s deviation from the median of the entire sample. That is, for a random variable `X`, the median absolute deviation is `median(|median(X) - X|)`.

::::{note} 
Like [`PERCENTILE`](esql-functions-operators.md#esql-percentile), `MEDIAN_ABSOLUTE_DEVIATION` is [usually approximate](esql-functions-operators.md#esql-percentile-approximate).
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS MEDIAN(salary), MEDIAN_ABSOLUTE_DEVIATION(salary)
```

| MEDIAN(salary):double | MEDIAN_ABSOLUTE_DEVIATION(salary):double |
| --- | --- |
| 47003 | 10096.5 |

The expression can use inline functions. For example, to calculate the median absolute deviation of the maximum values of a multivalued column, first use `MV_MAX` to get the maximum value per row, and use the result with the `MEDIAN_ABSOLUTE_DEVIATION` function

```esql
FROM employees
| STATS m_a_d_max_salary_change = MEDIAN_ABSOLUTE_DEVIATION(MV_MAX(salary_change))
```

| m_a_d_max_salary_change:double |
| --- |
| 5.69 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

::::{warning} 
`MEDIAN_ABSOLUTE_DEVIATION` is also [non-deterministic](https://en.wikipedia.org/wiki/Nondeterministic_algorithm). This means you can get slightly different results using the same data.

::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MIN` [esql-min] 

**Syntax**

:::{image} images/min.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

The minimum value of a field.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| date | date |
| date_nanos | date_nanos |
| double | double |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS MIN(languages)
```

| MIN(languages):integer |
| --- |
| 1 |

The expression can use inline functions. For example, to calculate the minimum over an average of a multivalued column, use `MV_AVG` to first average the multiple values per row, and use the result with the `MIN` function

```esql
FROM employees
| STATS min_avg_salary_change = MIN(MV_AVG(salary_change))
```

| min_avg_salary_change:double |
| --- |
| -8.46 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `PERCENTILE` [esql-percentile] 

**Syntax**

:::{image} images/percentile.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
`percentile`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

Returns the value at which a certain percentage of observed values occur. For example, the 95th percentile is the value which is greater than 95% of the observed values and the 50th percentile is the `MEDIAN`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | percentile | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | double |
| integer | long | double |
| long | double | double |
| long | integer | double |
| long | long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS p0 = PERCENTILE(salary,  0)
     , p50 = PERCENTILE(salary, 50)
     , p99 = PERCENTILE(salary, 99)
```

| p0:double | p50:double | p99:double |
| --- | --- | --- |
| 25324 | 47003 | 74970.29 |

The expression can use inline functions. For example, to calculate a percentile of the maximum values of a multivalued column, first use `MV_MAX` to get the maximum value per row, and use the result with the `PERCENTILE` function

```esql
FROM employees
| STATS p80_max_salary_change = PERCENTILE(MV_MAX(salary_change), 80)
```

| p80_max_salary_change:double |
| --- |
| 12.132 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


### `PERCENTILE` is (usually) approximate [esql-percentile-approximate] 

There are many different algorithms to calculate percentiles. The naive implementation simply stores all the values in a sorted array. To find the 50th percentile, you simply find the value that is at `my_array[count(my_array) * 0.5]`.

Clearly, the naive implementation does not scale — the sorted array grows linearly with the number of values in your dataset. To calculate percentiles across potentially billions of values in an Elasticsearch cluster, *approximate* percentiles are calculated.

The algorithm used by the `percentile` metric is called TDigest (introduced by Ted Dunning in [Computing Accurate Quantiles using T-Digests](https://github.com/tdunning/t-digest/blob/master/docs/t-digest-paper/histo.pdf)).

When using this metric, there are a few guidelines to keep in mind:

* Accuracy is proportional to `q(1-q)`. This means that extreme percentiles (e.g. 99%) are more accurate than less extreme percentiles, such as the median
* For small sets of values, percentiles are highly accurate (and potentially 100% accurate if the data is small enough).
* As the quantity of values in a bucket grows, the algorithm begins to approximate the percentiles. It is effectively trading accuracy for memory savings. The exact level of inaccuracy is difficult to generalize, since it depends on your data distribution and volume of data being aggregated

The following chart shows the relative error on a uniform distribution depending on the number of collected values and the requested percentile:

![percentiles error](images/percentiles_error.png "")

It shows how precision is better for extreme percentiles. The reason why error diminishes for large number of values is that the law of large numbers makes the distribution of values more and more uniform and the t-digest tree can do a better job at summarizing it. It would not be the case on more skewed distributions.

::::{warning} 
`PERCENTILE` is also [non-deterministic](https://en.wikipedia.org/wiki/Nondeterministic_algorithm). This means you can get slightly different results using the same data.

::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_CENTROID_AGG` [esql-st_centroid_agg] 

**Syntax**

:::{image} images/st_centroid_agg.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

Calculate the spatial centroid over a field with spatial point geometry type.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| cartesian_point | cartesian_point |
| geo_point | geo_point |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| STATS centroid=ST_CENTROID_AGG(location)
```

| centroid:geo_point |
| --- |
| POINT(-0.030548143003023033 24.37553649504829) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_EXTENT_AGG` [esql-st_extent_agg] 

**Syntax**

:::{image} images/st_extent_agg.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

Calculate the spatial extent over a field with geometry type. Returns a bounding box for all values of the field.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| cartesian_point | cartesian_shape |
| cartesian_shape | cartesian_shape |
| geo_point | geo_shape |
| geo_shape | geo_shape |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| WHERE country == "India"
| STATS extent = ST_EXTENT_AGG(location)
```

| extent:geo_shape |
| --- |
| BBOX (70.77995480038226, 91.5882289968431, 33.9830909203738, 8.47650992218405) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `STD_DEV` [esql-std_dev] 

**Syntax**

:::{image} images/std_dev.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

The standard deviation of a numeric field.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS STD_DEV(height)
```

| STD_DEV(height):double |
| --- |
| 0.20637044362020449 |

The expression can use inline functions. For example, to calculate the standard deviation of each employee’s maximum salary changes, first use `MV_MAX` on each row, and then use `STD_DEV` on the result

```esql
FROM employees
| STATS stddev_salary_change = STD_DEV(MV_MAX(salary_change))
```

| stddev_salary_change:double |
| --- |
| 6.875829592924112 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SUM` [esql-sum] 

**Syntax**

:::{image} images/sum.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

The sum of a numeric expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | long |
| long | long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| STATS SUM(languages)
```

| SUM(languages):long |
| --- |
| 281 |

The expression can use inline functions. For example, to calculate the sum of each employee’s maximum salary changes, apply the `MV_MAX` function to each row and then sum the results

```esql
FROM employees
| STATS total_salary_changes = SUM(MV_MAX(salary_change))
```

| total_salary_changes:double |
| --- |
| 446.75 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TOP` [esql-top] 

**Syntax**

:::{image} images/top.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   The field to collect the top values for.

`limit`
:   The maximum number of values to collect.

`order`
:   The order to calculate the top values. Either `asc` or `desc`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Collects the top values for a field. Includes repeated values.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | limit | order | result |
| --- | --- | --- | --- |
| boolean | integer | keyword | boolean |
| date | integer | keyword | date |
| double | integer | keyword | double |
| integer | integer | keyword | integer |
| ip | integer | keyword | ip |
| keyword | integer | keyword | keyword |
| long | integer | keyword | long |
| text | integer | keyword | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| STATS top_salaries = TOP(salary, 3, "desc"), top_salary = MAX(salary)
```

| top_salaries:integer | top_salary:integer |
| --- | --- |
| [74999, 74970, 74572] | 74999 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `VALUES` [esql-values] 

::::{warning} 
Do not use on production environments. This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


**Syntax**

:::{image} images/values.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

Returns all values in a group as a multivalued field. The order of the returned values isn’t guaranteed. If you need the values returned in order use [`MV_SORT`](esql-functions-operators.md#esql-mv_sort).

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| date | date |
| date_nanos | date_nanos |
| double | double |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
  FROM employees
| EVAL first_letter = SUBSTRING(first_name, 0, 1)
| STATS first_name=MV_SORT(VALUES(first_name)) BY first_letter
| SORT first_letter
```

| first_name:keyword | first_letter:keyword |
| --- | --- |
| [Alejandro, Amabile, Anneke, Anoosh, Arumugam] | A |
| [Basil, Berhard, Berni, Bezalel, Bojan, Breannda, Brendon] | B |
| [Charlene, Chirstian, Claudi, Cristinel] | C |
| [Danel, Divier, Domenick, Duangkaew] | D |
| [Ebbe, Eberhardt, Erez] | E |
| Florian | F |
| [Gao, Georgi, Georgy, Gino, Guoxiang] | G |
| [Heping, Hidefumi, Hilari, Hironobu, Hironoby, Hisao] | H |
| [Jayson, Jungsoon] | J |
| [Kazuhide, Kazuhito, Kendra, Kenroku, Kshitij, Kwee, Kyoichi] | K |
| [Lillian, Lucien] | L |
| [Magy, Margareta, Mary, Mayuko, Mayumi, Mingsen, Mokhtar, Mona, Moss] | M |
| Otmar | O |
| [Parto, Parviz, Patricio, Prasadram, Premal] | P |
| [Ramzi, Remzi, Reuven] | R |
| [Sailaja, Saniya, Sanjiv, Satosi, Shahaf, Shir, Somnath, Sreekrishna, Sudharsan, Sumant, Suzette] | S |
| [Tse, Tuval, Tzvetan] | T |
| [Udi, Uri] | U |
| [Valdiodio, Valter, Vishv] | V |
| Weiyi | W |
| Xinglin | X |
| [Yinghua, Yishay, Yongqiao] | Y |
| [Zhongwei, Zvonko] | Z |
| null | null |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

::::{warning} 
This can use a significant amount of memory and ES|QL doesn’t yet grow aggregations beyond memory. So this aggregation will work until it is used to collect more values than can fit into memory. Once it collects too many values it will fail the query with a [Circuit Breaker Error](circuit-breaker-errors.md).

::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `WEIGHTED_AVG` [esql-weighted_avg] 

**Syntax**

:::{image} images/weighted_avg.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   A numeric value.

`weight`
:   A numeric weight.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

The weighted average of a numeric expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | weight | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | double |
| integer | long | double |
| long | double | double |
| long | integer | double |
| long | long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| STATS w_avg = WEIGHTED_AVG(salary, height) by languages
| EVAL w_avg = ROUND(w_avg)
| KEEP w_avg, languages
| SORT languages
```

| w_avg:double | languages:integer |
| --- | --- |
| 51464.0 | 1 |
| 48477.0 | 2 |
| 52379.0 | 3 |
| 47990.0 | 4 |
| 42119.0 | 5 |
| 52142.0 | null |


## {{esql}} grouping functions [esql-group-functions]


The [`STATS`](esql-commands.md#esql-stats-by) command supports these grouping functions:

%  tag::group_list[]

* [`BUCKET`](esql-functions-operators.md#esql-bucket)
* [preview] [`CATEGORIZE`](esql-functions-operators.md#esql-categorize)

%  end::group_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `BUCKET` [esql-bucket] 

**Syntax**

:::{image} images/bucket.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Numeric or date expression from which to derive buckets.

`buckets`
:   Target number of buckets, or desired bucket size if `from` and `to` parameters are omitted.

`from`
:   Start of the range. Can be a number, a date or a date expressed as a string.

`to`
:   End of the range. Can be a number, a date or a date expressed as a string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Creates groups of values - buckets - out of a datetime or numeric input. The size of the buckets can either be provided directly, or chosen based on a recommended count and values range.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | buckets | from | to | result |
| --- | --- | --- | --- | --- |
| date | date_period |  |  | date |
| date | integer | date | date | date |
| date | integer | date | keyword | date |
| date | integer | date | text | date |
| date | integer | keyword | date | date |
| date | integer | keyword | keyword | date |
| date | integer | keyword | text | date |
| date | integer | text | date | date |
| date | integer | text | keyword | date |
| date | integer | text | text | date |
| date | time_duration |  |  | date |
| date_nanos | date_period |  |  | date_nanos |
| date_nanos | integer | date | date | date_nanos |
| date_nanos | integer | date | keyword | date_nanos |
| date_nanos | integer | date | text | date_nanos |
| date_nanos | integer | keyword | date | date_nanos |
| date_nanos | integer | keyword | keyword | date_nanos |
| date_nanos | integer | keyword | text | date_nanos |
| date_nanos | integer | text | date | date_nanos |
| date_nanos | integer | text | keyword | date_nanos |
| date_nanos | integer | text | text | date_nanos |
| date_nanos | time_duration |  |  | date_nanos |
| double | double |  |  | double |
| double | integer | double | double | double |
| double | integer | double | integer | double |
| double | integer | double | long | double |
| double | integer | integer | double | double |
| double | integer | integer | integer | double |
| double | integer | integer | long | double |
| double | integer | long | double | double |
| double | integer | long | integer | double |
| double | integer | long | long | double |
| double | integer |  |  | double |
| double | long |  |  | double |
| integer | double |  |  | double |
| integer | integer | double | double | double |
| integer | integer | double | integer | double |
| integer | integer | double | long | double |
| integer | integer | integer | double | double |
| integer | integer | integer | integer | double |
| integer | integer | integer | long | double |
| integer | integer | long | double | double |
| integer | integer | long | integer | double |
| integer | integer | long | long | double |
| integer | integer |  |  | double |
| integer | long |  |  | double |
| long | double |  |  | double |
| long | integer | double | double | double |
| long | integer | double | integer | double |
| long | integer | double | long | double |
| long | integer | integer | double | double |
| long | integer | integer | integer | double |
| long | integer | integer | long | double |
| long | integer | long | double | double |
| long | integer | long | integer | double |
| long | integer | long | long | double |
| long | integer |  |  | double |
| long | long |  |  | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

`BUCKET` can work in two modes: one in which the size of the bucket is computed based on a buckets count recommendation (four parameters) and a range, and another in which the bucket size is provided directly (two parameters).

Using a target number of buckets, a start of a range, and an end of a range, `BUCKET` picks an appropriate bucket size to generate the target number of buckets or fewer. For example, asking for at most 20 buckets over a year results in monthly buckets:

```esql
FROM employees
| WHERE hire_date >= "1985-01-01T00:00:00Z" AND hire_date < "1986-01-01T00:00:00Z"
| STATS hire_date = MV_SORT(VALUES(hire_date)) BY month = BUCKET(hire_date, 20, "1985-01-01T00:00:00Z", "1986-01-01T00:00:00Z")
| SORT hire_date
```

| hire_date:date | month:date |
| --- | --- |
| [1985-02-18T00:00:00.000Z, 1985-02-24T00:00:00.000Z] | 1985-02-01T00:00:00.000Z |
| 1985-05-13T00:00:00.000Z | 1985-05-01T00:00:00.000Z |
| 1985-07-09T00:00:00.000Z | 1985-07-01T00:00:00.000Z |
| 1985-09-17T00:00:00.000Z | 1985-09-01T00:00:00.000Z |
| [1985-10-14T00:00:00.000Z, 1985-10-20T00:00:00.000Z] | 1985-10-01T00:00:00.000Z |
| [1985-11-19T00:00:00.000Z, 1985-11-20T00:00:00.000Z, 1985-11-21T00:00:00.000Z] | 1985-11-01T00:00:00.000Z |

The goal isn’t to provide **exactly** the target number of buckets, it’s to pick a range that people are comfortable with that provides at most the target number of buckets.

Combine `BUCKET` with an [aggregation](esql-functions-operators.md#esql-agg-functions) to create a histogram:

```esql
FROM employees
| WHERE hire_date >= "1985-01-01T00:00:00Z" AND hire_date < "1986-01-01T00:00:00Z"
| STATS hires_per_month = COUNT(*) BY month = BUCKET(hire_date, 20, "1985-01-01T00:00:00Z", "1986-01-01T00:00:00Z")
| SORT month
```

| hires_per_month:long | month:date |
| --- | --- |
| 2 | 1985-02-01T00:00:00.000Z |
| 1 | 1985-05-01T00:00:00.000Z |
| 1 | 1985-07-01T00:00:00.000Z |
| 1 | 1985-09-01T00:00:00.000Z |
| 2 | 1985-10-01T00:00:00.000Z |
| 4 | 1985-11-01T00:00:00.000Z |

::::{note} 
`BUCKET` does not create buckets that don’t match any documents. That’s why this example is missing `1985-03-01` and other dates.
::::


Asking for more buckets can result in a smaller range. For example, asking for at most 100 buckets in a year results in weekly buckets:

```esql
FROM employees
| WHERE hire_date >= "1985-01-01T00:00:00Z" AND hire_date < "1986-01-01T00:00:00Z"
| STATS hires_per_week = COUNT(*) BY week = BUCKET(hire_date, 100, "1985-01-01T00:00:00Z", "1986-01-01T00:00:00Z")
| SORT week
```

| hires_per_week:long | week:date |
| --- | --- |
| 2 | 1985-02-18T00:00:00.000Z |
| 1 | 1985-05-13T00:00:00.000Z |
| 1 | 1985-07-08T00:00:00.000Z |
| 1 | 1985-09-16T00:00:00.000Z |
| 2 | 1985-10-14T00:00:00.000Z |
| 4 | 1985-11-18T00:00:00.000Z |

::::{note} 
`BUCKET` does not filter any rows. It only uses the provided range to pick a good bucket size. For rows with a value outside of the range, it returns a bucket value that corresponds to a bucket outside the range. Combine`BUCKET` with [`WHERE`](esql-commands.md#esql-where) to filter rows.
::::


If the desired bucket size is known in advance, simply provide it as the second argument, leaving the range out:

```esql
FROM employees
| WHERE hire_date >= "1985-01-01T00:00:00Z" AND hire_date < "1986-01-01T00:00:00Z"
| STATS hires_per_week = COUNT(*) BY week = BUCKET(hire_date, 1 week)
| SORT week
```

| hires_per_week:long | week:date |
| --- | --- |
| 2 | 1985-02-18T00:00:00.000Z |
| 1 | 1985-05-13T00:00:00.000Z |
| 1 | 1985-07-08T00:00:00.000Z |
| 1 | 1985-09-16T00:00:00.000Z |
| 2 | 1985-10-14T00:00:00.000Z |
| 4 | 1985-11-18T00:00:00.000Z |

::::{note} 
When providing the bucket size as the second parameter, it must be a time duration or date period.
::::


`BUCKET` can also operate on numeric fields. For example, to create a salary histogram:

```esql
FROM employees
| STATS COUNT(*) by bs = BUCKET(salary, 20, 25324, 74999)
| SORT bs
```

| COUNT(*):long | bs:double |
| --- | --- |
| 9 | 25000.0 |
| 9 | 30000.0 |
| 18 | 35000.0 |
| 11 | 40000.0 |
| 11 | 45000.0 |
| 10 | 50000.0 |
| 7 | 55000.0 |
| 9 | 60000.0 |
| 8 | 65000.0 |
| 8 | 70000.0 |

Unlike the earlier example that intentionally filters on a date range, you rarely want to filter on a numeric range. You have to find the `min` and `max` separately. {{esql}} doesn’t yet have an easy way to do that automatically.

The range can be omitted if the desired bucket size is known in advance. Simply provide it as the second argument:

```esql
FROM employees
| WHERE hire_date >= "1985-01-01T00:00:00Z" AND hire_date < "1986-01-01T00:00:00Z"
| STATS c = COUNT(1) BY b = BUCKET(salary, 5000.)
| SORT b
```

| c:long | b:double |
| --- | --- |
| 1 | 25000.0 |
| 1 | 30000.0 |
| 1 | 40000.0 |
| 2 | 45000.0 |
| 2 | 50000.0 |
| 1 | 55000.0 |
| 1 | 60000.0 |
| 1 | 65000.0 |
| 1 | 70000.0 |

Create hourly buckets for the last 24 hours, and calculate the number of events per hour:

```esql
FROM sample_data
| WHERE @timestamp >= NOW() - 1 day and @timestamp < NOW()
| STATS COUNT(*) BY bucket = BUCKET(@timestamp, 25, NOW() - 1 day, NOW())
```

| COUNT(*):long | bucket:date |
| --- | --- |

Create monthly buckets for the year 1985, and calculate the average salary by hiring month

```esql
FROM employees
| WHERE hire_date >= "1985-01-01T00:00:00Z" AND hire_date < "1986-01-01T00:00:00Z"
| STATS AVG(salary) BY bucket = BUCKET(hire_date, 20, "1985-01-01T00:00:00Z", "1986-01-01T00:00:00Z")
| SORT bucket
```

| AVG(salary):double | bucket:date |
| --- | --- |
| 46305.0 | 1985-02-01T00:00:00.000Z |
| 44817.0 | 1985-05-01T00:00:00.000Z |
| 62405.0 | 1985-07-01T00:00:00.000Z |
| 49095.0 | 1985-09-01T00:00:00.000Z |
| 51532.0 | 1985-10-01T00:00:00.000Z |
| 54539.75 | 1985-11-01T00:00:00.000Z |

`BUCKET` may be used in both the aggregating and grouping part of the [STATS …​ BY …​](esql-commands.md#esql-stats-by) command provided that in the aggregating part the function is referenced by an alias defined in the grouping part, or that it is invoked with the exact same expression:

```esql
FROM employees
| STATS s1 = b1 + 1, s2 = BUCKET(salary / 1000 + 999, 50.) + 2 BY b1 = BUCKET(salary / 100 + 99, 50.), b2 = BUCKET(salary / 1000 + 999, 50.)
| SORT b1, b2
| KEEP s1, b1, s2, b2
```

| s1:double | b1:double | s2:double | b2:double |
| --- | --- | --- | --- |
| 351.0 | 350.0 | 1002.0 | 1000.0 |
| 401.0 | 400.0 | 1002.0 | 1000.0 |
| 451.0 | 450.0 | 1002.0 | 1000.0 |
| 501.0 | 500.0 | 1002.0 | 1000.0 |
| 551.0 | 550.0 | 1002.0 | 1000.0 |
| 601.0 | 600.0 | 1002.0 | 1000.0 |
| 601.0 | 600.0 | 1052.0 | 1050.0 |
| 651.0 | 650.0 | 1052.0 | 1050.0 |
| 701.0 | 700.0 | 1052.0 | 1050.0 |
| 751.0 | 750.0 | 1052.0 | 1050.0 |
| 801.0 | 800.0 | 1052.0 | 1050.0 |

Sometimes you need to change the start value of each bucket by a given duration (similar to date histogram aggregation’s [`offset`](search-aggregations-bucket-histogram-aggregation.md) parameter). To do so, you will need to take into account how the language handles expressions within the `STATS` command: if these contain functions or arithmetic operators, a virtual `EVAL` is inserted before and/or after the `STATS` command. Consequently, a double compensation is needed to adjust the bucketed date value before the aggregation and then again after. For instance, inserting a negative offset of `1 hour` to buckets of `1 year` looks like this:

```esql
FROM employees
| STATS dates = MV_SORT(VALUES(birth_date)) BY b = BUCKET(birth_date + 1 HOUR, 1 YEAR) - 1 HOUR
| EVAL d_count = MV_COUNT(dates)
| SORT d_count, b
| LIMIT 3
```

| dates:date | b:date | d_count:integer |
| --- | --- | --- |
| 1965-01-03T00:00:00.000Z | 1964-12-31T23:00:00.000Z | 1 |
| [1955-01-21T00:00:00.000Z, 1955-08-20T00:00:00.000Z, 1955-08-28T00:00:00.000Z, 1955-10-04T00:00:00.000Z] | 1954-12-31T23:00:00.000Z | 4 |
| [1957-04-04T00:00:00.000Z, 1957-05-23T00:00:00.000Z, 1957-05-25T00:00:00.000Z, 1957-12-03T00:00:00.000Z] | 1956-12-31T23:00:00.000Z | 4 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `CATEGORIZE` [esql-categorize] 

::::{warning} 
Do not use on production environments. This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


**Syntax**

:::{image} images/categorize.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Expression to categorize

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Groups text messages into categories of similarly formatted text values.

`CATEGORIZE` has the following limitations:

* can’t be used within other expressions
* can’t be used with multiple groupings
* can’t be used or referenced within aggregate functions

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

This example categorizes server logs messages into categories and aggregates their counts.

```esql
FROM sample_data
| STATS count=COUNT() BY category=CATEGORIZE(message)
```

| count:long | category:keyword |
| --- | --- |
| 3 | .**?Connected.+?to.**? |
| 3 | .**?Connection.+?error.**? |
| 1 | .**?Disconnected.**? |


## {{esql}} conditional functions and expressions [esql-conditional-functions-and-expressions]


Conditional functions return one of their arguments by evaluating in an if-else manner. {{esql}} supports these conditional functions:

%  tag::cond_list[]

* [`CASE`](esql-functions-operators.md#esql-case)
* [`COALESCE`](esql-functions-operators.md#esql-coalesce)
* [`GREATEST`](esql-functions-operators.md#esql-greatest)
* [`LEAST`](esql-functions-operators.md#esql-least)

%  end::cond_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `CASE` [esql-case] 

**Syntax**

:::{image} images/case.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`condition`
:   A condition.

`trueValue`
:   The value that’s returned when the corresponding condition is the first to evaluate to `true`. The default value is returned when no condition matches.

`elseValue`
:   The value that’s returned when no condition evaluates to `true`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Accepts pairs of conditions and values. The function returns the value that belongs to the first condition that evaluates to `true`.  If the number of arguments is odd, the last argument is the default value which is returned when no condition matches. If the number of arguments is even, and no condition matches, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| condition | trueValue | elseValue | result |
| --- | --- | --- | --- |
| boolean | boolean | boolean | boolean |
| boolean | boolean |  | boolean |
| boolean | cartesian_point | cartesian_point | cartesian_point |
| boolean | cartesian_point |  | cartesian_point |
| boolean | cartesian_shape | cartesian_shape | cartesian_shape |
| boolean | cartesian_shape |  | cartesian_shape |
| boolean | date | date | date |
| boolean | date |  | date |
| boolean | date_nanos | date_nanos | date_nanos |
| boolean | date_nanos |  | date_nanos |
| boolean | double | double | double |
| boolean | double |  | double |
| boolean | geo_point | geo_point | geo_point |
| boolean | geo_point |  | geo_point |
| boolean | geo_shape | geo_shape | geo_shape |
| boolean | geo_shape |  | geo_shape |
| boolean | integer | integer | integer |
| boolean | integer |  | integer |
| boolean | ip | ip | ip |
| boolean | ip |  | ip |
| boolean | keyword | keyword | keyword |
| boolean | keyword | text | keyword |
| boolean | keyword |  | keyword |
| boolean | long | long | long |
| boolean | long |  | long |
| boolean | text | keyword | keyword |
| boolean | text | text | keyword |
| boolean | text |  | keyword |
| boolean | unsigned_long | unsigned_long | unsigned_long |
| boolean | unsigned_long |  | unsigned_long |
| boolean | version | version | version |
| boolean | version |  | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

Determine whether employees are monolingual, bilingual, or polyglot:

```esql
FROM employees
| EVAL type = CASE(
    languages <= 1, "monolingual",
    languages <= 2, "bilingual",
     "polyglot")
| KEEP emp_no, languages, type
```

| emp_no:integer | languages:integer | type:keyword |
| --- | --- | --- |
| 10001 | 2 | bilingual |
| 10002 | 5 | polyglot |
| 10003 | 4 | polyglot |
| 10004 | 5 | polyglot |
| 10005 | 1 | monolingual |

Calculate the total connection success rate based on log messages:

```esql
FROM sample_data
| EVAL successful = CASE(
    STARTS_WITH(message, "Connected to"), 1,
    message == "Connection error", 0
  )
| STATS success_rate = AVG(successful)
```

| success_rate:double |
| --- |
| 0.5 |

Calculate an hourly error rate as a percentage of the total number of log messages:

```esql
FROM sample_data
| EVAL error = CASE(message LIKE "*error*", 1, 0)
| EVAL hour = DATE_TRUNC(1 hour, @timestamp)
| STATS error_rate = AVG(error) by hour
| SORT hour
```

| error_rate:double | hour:date |
| --- | --- |
| 0.0 | 2023-10-23T12:00:00.000Z |
| 0.6 | 2023-10-23T13:00:00.000Z |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `COALESCE` [esql-coalesce] 

**Syntax**

:::{image} images/coalesce.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`first`
:   Expression to evaluate.

`rest`
:   Other expression to evaluate.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the first of its arguments that is not null. If all arguments are null, it returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| first | rest | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| boolean |  | boolean |
| cartesian_point | cartesian_point | cartesian_point |
| cartesian_shape | cartesian_shape | cartesian_shape |
| date | date | date |
| date_nanos | date_nanos | date_nanos |
| geo_point | geo_point | geo_point |
| geo_shape | geo_shape | geo_shape |
| integer | integer | integer |
| integer |  | integer |
| ip | ip | ip |
| keyword | keyword | keyword |
| keyword |  | keyword |
| long | long | long |
| long |  | long |
| text | text | keyword |
| text |  | keyword |
| version | version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=null, b="b"
| EVAL COALESCE(a, b)
```

| a:null | b:keyword | COALESCE(a, b):keyword |
| --- | --- | --- |
| null | b | b |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `GREATEST` [esql-greatest] 

**Syntax**

:::{image} images/greatest.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`first`
:   First of the columns to evaluate.

`rest`
:   The rest of the columns to evaluate.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the maximum value from multiple columns. This is similar to [`MV_MAX`](esql-functions-operators.md#esql-mv_max) except it is intended to run on multiple columns at once.

::::{note} 
When run on `keyword` or `text` fields, this returns the last string in alphabetical order. When run on `boolean` columns this will return `true` if any values are `true`.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| first | rest | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| boolean |  | boolean |
| date | date | date |
| date_nanos | date_nanos | date_nanos |
| double | double | double |
| integer | integer | integer |
| integer |  | integer |
| ip | ip | ip |
| keyword | keyword | keyword |
| keyword |  | keyword |
| long | long | long |
| long |  | long |
| text | text | keyword |
| text |  | keyword |
| version | version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = 10, b = 20
| EVAL g = GREATEST(a, b)
```

| a:integer | b:integer | g:integer |
| --- | --- | --- |
| 10 | 20 | 20 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LEAST` [esql-least] 

**Syntax**

:::{image} images/least.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`first`
:   First of the columns to evaluate.

`rest`
:   The rest of the columns to evaluate.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the minimum value from multiple columns. This is similar to [`MV_MIN`](esql-functions-operators.md#esql-mv_min) except it is intended to run on multiple columns at once.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| first | rest | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| boolean |  | boolean |
| date | date | date |
| date_nanos | date_nanos | date_nanos |
| double | double | double |
| integer | integer | integer |
| integer |  | integer |
| ip | ip | ip |
| keyword | keyword | keyword |
| keyword |  | keyword |
| long | long | long |
| long |  | long |
| text | text | keyword |
| text |  | keyword |
| version | version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = 10, b = 20
| EVAL l = LEAST(a, b)
```

| a:integer | b:integer | l:integer |
| --- | --- | --- |
| 10 | 20 | 10 |


## {{esql}} date-time functions [esql-date-time-functions]


{{esql}} supports these date-time functions:

%  tag::date_list[]

* [`DATE_DIFF`](esql-functions-operators.md#esql-date_diff)
* [`DATE_EXTRACT`](esql-functions-operators.md#esql-date_extract)
* [`DATE_FORMAT`](esql-functions-operators.md#esql-date_format)
* [`DATE_PARSE`](esql-functions-operators.md#esql-date_parse)
* [`DATE_TRUNC`](esql-functions-operators.md#esql-date_trunc)
* [`NOW`](esql-functions-operators.md#esql-now)

%  end::date_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `DATE_DIFF` [esql-date_diff] 

**Syntax**

:::{image} images/date_diff.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`unit`
:   Time difference unit

`startTimestamp`
:   A string representing a start timestamp

`endTimestamp`
:   A string representing an end timestamp

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Subtracts the `startTimestamp` from the `endTimestamp` and returns the difference in multiples of `unit`. If `startTimestamp` is later than the `endTimestamp`, negative values are returned.

| Datetime difference units |
| --- |
| **unit** | **abbreviations** |
| year | years, yy, yyyy |
| quarter | quarters, qq, q |
| month | months, mm, m |
| dayofyear | dy, y |
| day | days, dd, d |
| week | weeks, wk, ww |
| weekday | weekdays, dw |
| hour | hours, hh |
| minute | minutes, mi, n |
| second | seconds, ss, s |
| millisecond | milliseconds, ms |
| microsecond | microseconds, mcs |
| nanosecond | nanoseconds, ns |

Note that while there is an overlap between the function’s supported units and {{esql}}'s supported time span literals, these sets are distinct and not interchangeable. Similarly, the supported abbreviations are conveniently shared with implementations of this function in other established products and not necessarily common with the date-time nomenclature used by {{es}}.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| unit | startTimestamp | endTimestamp | result |
| --- | --- | --- | --- |
| keyword | date | date | integer |
| keyword | date | date_nanos | integer |
| keyword | date_nanos | date | integer |
| keyword | date_nanos | date_nanos | integer |
| text | date | date | integer |
| text | date | date_nanos | integer |
| text | date_nanos | date | integer |
| text | date_nanos | date_nanos | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW date1 = TO_DATETIME("2023-12-02T11:00:00.000Z"), date2 = TO_DATETIME("2023-12-02T11:00:00.001Z")
| EVAL dd_ms = DATE_DIFF("microseconds", date1, date2)
```

| date1:date | date2:date | dd_ms:integer |
| --- | --- | --- |
| 2023-12-02T11:00:00.000Z | 2023-12-02T11:00:00.001Z | 1000 |

When subtracting in calendar units - like year, month a.s.o. - only the fully elapsed units are counted. To avoid this and obtain also remainders, simply switch to the next smaller unit and do the date math accordingly.

```esql
ROW end_23=TO_DATETIME("2023-12-31T23:59:59.999Z"),
  start_24=TO_DATETIME("2024-01-01T00:00:00.000Z"),
    end_24=TO_DATETIME("2024-12-31T23:59:59.999")
| EVAL end23_to_start24=DATE_DIFF("year", end_23, start_24)
| EVAL end23_to_end24=DATE_DIFF("year", end_23, end_24)
| EVAL start_to_end_24=DATE_DIFF("year", start_24, end_24)
```

| end_23:date | start_24:date | end_24:date | end23_to_start24:integer | end23_to_end24:integer | start_to_end_24:integer |
| --- | --- | --- | --- | --- | --- |
| 2023-12-31T23:59:59.999Z | 2024-01-01T00:00:00.000Z | 2024-12-31T23:59:59.999Z | 0 | 1 | 0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `DATE_EXTRACT` [esql-date_extract] 

**Syntax**

:::{image} images/date_extract.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`datePart`
:   Part of the date to extract.  Can be: `aligned_day_of_week_in_month`, `aligned_day_of_week_in_year`, `aligned_week_of_month`, `aligned_week_of_year`, `ampm_of_day`, `clock_hour_of_ampm`, `clock_hour_of_day`, `day_of_month`, `day_of_week`, `day_of_year`, `epoch_day`, `era`, `hour_of_ampm`, `hour_of_day`, `instant_seconds`, `micro_of_day`, `micro_of_second`, `milli_of_day`, `milli_of_second`, `minute_of_day`, `minute_of_hour`, `month_of_year`, `nano_of_day`, `nano_of_second`, `offset_seconds`, `proleptic_month`, `second_of_day`, `second_of_minute`, `year`, or `year_of_era`. Refer to [java.time.temporal.ChronoField](https://docs.oracle.com/javase/8/docs/api/java/time/temporal/ChronoField.md) for a description of these values.  If `null`, the function returns `null`.

`date`
:   Date expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts parts of a date, like year, month, day, hour.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| datePart | date | result |
| --- | --- | --- |
| keyword | date | long |
| keyword | date_nanos | long |
| text | date | long |
| text | date_nanos | long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW date = DATE_PARSE("yyyy-MM-dd", "2022-05-06")
| EVAL year = DATE_EXTRACT("year", date)
```

| date:date | year:long |
| --- | --- |
| 2022-05-06T00:00:00.000Z | 2022 |

Find all events that occurred outside of business hours (before 9 AM or after 5PM), on any given date:

```esql
FROM sample_data
| WHERE DATE_EXTRACT("hour_of_day", @timestamp) < 9 AND DATE_EXTRACT("hour_of_day", @timestamp) >= 17
```

| @timestamp:date | client_ip:ip | event_duration:long | message:keyword |
| --- | --- | --- | --- |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `DATE_FORMAT` [esql-date_format] 

**Syntax**

:::{image} images/date_format.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`dateFormat`
:   Date format (optional).  If no format is specified, the `yyyy-MM-dd'T'HH:mm:ss.SSSZ` format is used. If `null`, the function returns `null`.

`date`
:   Date expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a string representation of a date, in the provided format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| dateFormat | date | result |
| --- | --- | --- |
| date |  | keyword |
| date_nanos |  | keyword |
| keyword | date | keyword |
| keyword | date_nanos | keyword |
| text | date | keyword |
| text | date_nanos | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP first_name, last_name, hire_date
| EVAL hired = DATE_FORMAT("yyyy-MM-dd", hire_date)
```

| first_name:keyword | last_name:keyword | hire_date:date | hired:keyword |
| --- | --- | --- | --- |
| Alejandro | McAlpine | 1991-06-26T00:00:00.000Z | 1991-06-26 |
| Amabile | Gomatam | 1992-11-18T00:00:00.000Z | 1992-11-18 |
| Anneke | Preusig | 1989-06-02T00:00:00.000Z | 1989-06-02 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `DATE_PARSE` [esql-date_parse] 

**Syntax**

:::{image} images/date_parse.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`datePattern`
:   The date format. Refer to the [`DateTimeFormatter` documentation](https://docs.oracle.com/en/java/javase/14/docs/api/java.base/java/time/format/DateTimeFormatter.md) for the syntax. If `null`, the function returns `null`.

`dateString`
:   Date expression as a string. If `null` or an empty string, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a date by parsing the second argument using the format specified in the first argument.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| datePattern | dateString | result |
| --- | --- | --- |
| keyword | keyword | date |
| keyword | text | date |
| text | keyword | date |
| text | text | date |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW date_string = "2022-05-06"
| EVAL date = DATE_PARSE("yyyy-MM-dd", date_string)
```

| date_string:keyword | date:date |
| --- | --- |
| 2022-05-06 | 2022-05-06T00:00:00.000Z |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `DATE_TRUNC` [esql-date_trunc] 

**Syntax**

:::{image} images/date_trunc.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`interval`
:   Interval; expressed using the timespan literal syntax.

`date`
:   Date expression

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Rounds down a date to the closest interval.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| interval | date | result |
| --- | --- | --- |
| date_period | date | date |
| date_period | date_nanos | date_nanos |
| time_duration | date | date |
| time_duration | date_nanos | date_nanos |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM employees
| KEEP first_name, last_name, hire_date
| EVAL year_hired = DATE_TRUNC(1 year, hire_date)
```

| first_name:keyword | last_name:keyword | hire_date:date | year_hired:date |
| --- | --- | --- | --- |
| Alejandro | McAlpine | 1991-06-26T00:00:00.000Z | 1991-01-01T00:00:00.000Z |
| Amabile | Gomatam | 1992-11-18T00:00:00.000Z | 1992-01-01T00:00:00.000Z |
| Anneke | Preusig | 1989-06-02T00:00:00.000Z | 1989-01-01T00:00:00.000Z |

Combine `DATE_TRUNC` with [`STATS`](esql-commands.md#esql-stats-by) to create date histograms. For example, the number of hires per year:

```esql
FROM employees
| EVAL year = DATE_TRUNC(1 year, hire_date)
| STATS hires = COUNT(emp_no) BY year
| SORT year
```

| hires:long | year:date |
| --- | --- |
| 11 | 1985-01-01T00:00:00.000Z |
| 11 | 1986-01-01T00:00:00.000Z |
| 15 | 1987-01-01T00:00:00.000Z |
| 9 | 1988-01-01T00:00:00.000Z |
| 13 | 1989-01-01T00:00:00.000Z |
| 12 | 1990-01-01T00:00:00.000Z |
| 6 | 1991-01-01T00:00:00.000Z |
| 8 | 1992-01-01T00:00:00.000Z |
| 3 | 1993-01-01T00:00:00.000Z |
| 4 | 1994-01-01T00:00:00.000Z |
| 5 | 1995-01-01T00:00:00.000Z |
| 1 | 1996-01-01T00:00:00.000Z |
| 1 | 1997-01-01T00:00:00.000Z |
| 1 | 1999-01-01T00:00:00.000Z |

Or an hourly error rate:

```esql
FROM sample_data
| EVAL error = CASE(message LIKE "*error*", 1, 0)
| EVAL hour = DATE_TRUNC(1 hour, @timestamp)
| STATS error_rate = AVG(error) by hour
| SORT hour
```

| error_rate:double | hour:date |
| --- | --- |
| 0.0 | 2023-10-23T12:00:00.000Z |
| 0.6 | 2023-10-23T13:00:00.000Z |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `NOW` [esql-now] 

**Syntax**

:::{image} images/now.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns current date and time.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| result |
| --- |
| date |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW current_date = NOW()
```

| y:keyword |
| --- |
| 20 |

To retrieve logs from the last hour:

```esql
FROM sample_data
| WHERE @timestamp > NOW() - 1 hour
```

| @timestamp:date | client_ip:ip | event_duration:long | message:keyword |
| --- | --- | --- | --- |


## {{esql}} IP functions [esql-ip-functions]


{{esql}} supports these IP functions:

%  tag::ip_list[]

* [`CIDR_MATCH`](esql-functions-operators.md#esql-cidr_match)
* [`IP_PREFIX`](esql-functions-operators.md#esql-ip_prefix)

%  end::ip_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `CIDR_MATCH` [esql-cidr_match] 

**Syntax**

:::{image} images/cidr_match.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`ip`
:   IP address of type `ip` (both IPv4 and IPv6 are supported).

`blockX`
:   CIDR block to test the IP against.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns true if the provided IP is contained in one of the provided CIDR blocks.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| ip | blockX | result |
| --- | --- | --- |
| ip | keyword | boolean |
| ip | text | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM hosts
| WHERE CIDR_MATCH(ip1, "127.0.0.2/32", "127.0.0.3/32")
| KEEP card, host, ip0, ip1
```

| card:keyword | host:keyword | ip0:ip | ip1:ip |
| --- | --- | --- | --- |
| eth1 | beta | 127.0.0.1 | 127.0.0.2 |
| eth0 | gamma | fe80::cae2:65ff:fece:feb9 | 127.0.0.3 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `IP_PREFIX` [esql-ip_prefix] 

**Syntax**

:::{image} images/ip_prefix.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`ip`
:   IP address of type `ip` (both IPv4 and IPv6 are supported).

`prefixLengthV4`
:   Prefix length for IPv4 addresses.

`prefixLengthV6`
:   Prefix length for IPv6 addresses.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Truncates an IP to a given prefix length.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| ip | prefixLengthV4 | prefixLengthV6 | result |
| --- | --- | --- | --- |
| ip | integer | integer | ip |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
row ip4 = to_ip("1.2.3.4"), ip6 = to_ip("fe80::cae2:65ff:fece:feb9")
| eval ip4_prefix = ip_prefix(ip4, 24, 0), ip6_prefix = ip_prefix(ip6, 0, 112);
```

| ip4:ip | ip6:ip | ip4_prefix:ip | ip6_prefix:ip |
| --- | --- | --- | --- |
| 1.2.3.4 | fe80::cae2:65ff:fece:feb9 | 1.2.3.0 | fe80::cae2:65ff:fece:0000 |


## {{esql}} mathematical functions [esql-math-functions]


{{esql}} supports these mathematical functions:

%  tag::math_list[]

* [`ABS`](esql-functions-operators.md#esql-abs)
* [`ACOS`](esql-functions-operators.md#esql-acos)
* [`ASIN`](esql-functions-operators.md#esql-asin)
* [`ATAN`](esql-functions-operators.md#esql-atan)
* [`ATAN2`](esql-functions-operators.md#esql-atan2)
* [`CBRT`](esql-functions-operators.md#esql-cbrt)
* [`CEIL`](esql-functions-operators.md#esql-ceil)
* [`COS`](esql-functions-operators.md#esql-cos)
* [`COSH`](esql-functions-operators.md#esql-cosh)
* [`E`](esql-functions-operators.md#esql-e)
* [`EXP`](esql-functions-operators.md#esql-exp)
* [`FLOOR`](esql-functions-operators.md#esql-floor)
* [`HYPOT`](esql-functions-operators.md#esql-hypot)
* [`LOG`](esql-functions-operators.md#esql-log)
* [`LOG10`](esql-functions-operators.md#esql-log10)
* [`PI`](esql-functions-operators.md#esql-pi)
* [`POW`](esql-functions-operators.md#esql-pow)
* [`ROUND`](esql-functions-operators.md#esql-round)
* [`SIGNUM`](esql-functions-operators.md#esql-signum)
* [`SIN`](esql-functions-operators.md#esql-sin)
* [`SINH`](esql-functions-operators.md#esql-sinh)
* [`SQRT`](esql-functions-operators.md#esql-sqrt)
* [`TAN`](esql-functions-operators.md#esql-tan)
* [`TANH`](esql-functions-operators.md#esql-tanh)
* [`TAU`](esql-functions-operators.md#esql-tau)

%  end::math_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ABS` [esql-abs] 

**Syntax**

:::{image} images/abs.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the absolute value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | integer |
| long | long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW number = -1.0
| EVAL abs_number = ABS(number)
```

| number:double | abs_number:double |
| --- | --- |
| -1.0 | 1.0 |

```esql
FROM employees
| KEEP first_name, last_name, height
| EVAL abs_height = ABS(0.0 - height)
```

| first_name:keyword | last_name:keyword | height:double | abs_height:double |
| --- | --- | --- | --- |
| Alejandro | McAlpine | 1.48 | 1.48 |
| Amabile | Gomatam | 2.09 | 2.09 |
| Anneke | Preusig | 1.56 | 1.56 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ACOS` [esql-acos] 

**Syntax**

:::{image} images/acos.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Number between -1 and 1. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [arccosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of `n` as an angle, expressed in radians.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=.9
| EVAL acos=ACOS(a)
```

| a:double | acos:double |
| --- | --- |
| .9 | 0.45102681179626236 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ASIN` [esql-asin] 

**Syntax**

:::{image} images/asin.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Number between -1 and 1. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [arcsine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input numeric expression as an angle, expressed in radians.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=.9
| EVAL asin=ASIN(a)
```

| a:double | asin:double |
| --- | --- |
| .9 | 1.1197695149986342 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ATAN` [esql-atan] 

**Syntax**

:::{image} images/atan.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [arctangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input numeric expression as an angle, expressed in radians.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=12.9
| EVAL atan=ATAN(a)
```

| a:double | atan:double |
| --- | --- |
| 12.9 | 1.4934316673669235 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ATAN2` [esql-atan2] 

**Syntax**

:::{image} images/atan2.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`y_coordinate`
:   y coordinate. If `null`, the function returns `null`.

`x_coordinate`
:   x coordinate. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

The [angle](https://en.wikipedia.org/wiki/Atan2) between the positive x-axis and the ray from the origin to the point (x , y) in the Cartesian plane, expressed in radians.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| y_coordinate | x_coordinate | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| double | unsigned_long | double |
| integer | double | double |
| integer | integer | double |
| integer | long | double |
| integer | unsigned_long | double |
| long | double | double |
| long | integer | double |
| long | long | double |
| long | unsigned_long | double |
| unsigned_long | double | double |
| unsigned_long | integer | double |
| unsigned_long | long | double |
| unsigned_long | unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW y=12.9, x=.6
| EVAL atan2=ATAN2(y, x)
```

| y:double | x:double | atan2:double |
| --- | --- | --- |
| 12.9 | 0.6 | 1.5243181954438936 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `CBRT` [esql-cbrt] 

**Syntax**

:::{image} images/cbrt.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the cube root of a number. The input can be any numeric value, the return value is always a double. Cube roots of infinities are null.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW d = 1000.0
| EVAL c = cbrt(d)
```

| d: double | c:double |
| --- | --- |
| 1000.0 | 10.0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `CEIL` [esql-ceil] 

**Syntax**

:::{image} images/ceil.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Round a number up to the nearest integer.

::::{note} 
This is a noop for `long` (including unsigned) and `integer`. For `double` this picks the closest `double` value to the integer similar to [Math.ceil](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Math.md#ceil(double)).
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | integer |
| long | long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL a=CEIL(a)
```

| a:double |
| --- |
| 2 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `COS` [esql-cos] 

**Syntax**

:::{image} images/cos.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`angle`
:   An angle, in radians. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [cosine](https://en.wikipedia.org/wiki/Sine_and_cosine) of an angle.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| angle | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL cos=COS(a)
```

| a:double | cos:double |
| --- | --- |
| 1.8 | -0.2272020946930871 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `COSH` [esql-cosh] 

**Syntax**

:::{image} images/cosh.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [hyperbolic cosine](https://en.wikipedia.org/wiki/Hyperbolic_functions) of a number.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL cosh=COSH(a)
```

| a:double | cosh:double |
| --- | --- |
| 1.8 | 3.1074731763172667 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `E` [esql-e] 

**Syntax**

:::{image} images/e.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns [Euler’s number](https://en.wikipedia.org/wiki/E_(mathematical_constant)).

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| result |
| --- |
| double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW E()
```

| E():double |
| --- |
| 2.718281828459045 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `EXP` [esql-exp] 

**Syntax**

:::{image} images/exp.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the value of e raised to the power of the given number.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW d = 5.0
| EVAL s = EXP(d)
```

| d: double | s:double |
| --- | --- |
| 5.0 | 148.413159102576603 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `FLOOR` [esql-floor] 

**Syntax**

:::{image} images/floor.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Round a number down to the nearest integer.

::::{note} 
This is a noop for `long` (including unsigned) and `integer`. For `double` this picks the closest `double` value to the integer similar to [Math.floor](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Math.md#floor(double)).
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | integer |
| long | long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL a=FLOOR(a)
```

| a:double |
| --- |
| 1 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `HYPOT` [esql-hypot] 

**Syntax**

:::{image} images/hypot.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number1`
:   Numeric expression. If `null`, the function returns `null`.

`number2`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the hypotenuse of two numbers. The input can be any numeric values, the return value is always a double. Hypotenuses of infinities are null.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number1 | number2 | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| double | unsigned_long | double |
| integer | double | double |
| integer | integer | double |
| integer | long | double |
| integer | unsigned_long | double |
| long | double | double |
| long | integer | double |
| long | long | double |
| long | unsigned_long | double |
| unsigned_long | double | double |
| unsigned_long | integer | double |
| unsigned_long | long | double |
| unsigned_long | unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = 3.0, b = 4.0
| EVAL c = HYPOT(a, b)
```

| a:double | b:double | c:double |
| --- | --- | --- |
| 3.0 | 4.0 | 5.0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LOG` [esql-log] 

**Syntax**

:::{image} images/log.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`base`
:   Base of logarithm. If `null`, the function returns `null`. If not provided, this function returns the natural logarithm (base e) of a value.

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the logarithm of a value to a base. The input can be any numeric value, the return value is always a double.  Logs of zero, negative numbers, and base of one return `null` as well as a warning.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| base | number | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| double | unsigned_long | double |
| double |  | double |
| integer | double | double |
| integer | integer | double |
| integer | long | double |
| integer | unsigned_long | double |
| integer |  | double |
| long | double | double |
| long | integer | double |
| long | long | double |
| long | unsigned_long | double |
| long |  | double |
| unsigned_long | double | double |
| unsigned_long | integer | double |
| unsigned_long | long | double |
| unsigned_long | unsigned_long | double |
| unsigned_long |  | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW base = 2.0, value = 8.0
| EVAL s = LOG(base, value)
```

| base: double | value: double | s:double |
| --- | --- | --- |
| 2.0 | 8.0 | 3.0 |

```esql
row value = 100
| EVAL s = LOG(value);
```

| value: integer | s:double |
| --- | --- |
| 100 | 4.605170185988092 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LOG10` [esql-log10] 

**Syntax**

:::{image} images/log10.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the logarithm of a value to base 10. The input can be any numeric value, the return value is always a double.  Logs of 0 and negative numbers return `null` as well as a warning.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW d = 1000.0
| EVAL s = LOG10(d)
```

| d: double | s:double |
| --- | --- |
| 1000.0 | 3.0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `PI` [esql-pi] 

**Syntax**

:::{image} images/pi.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns [Pi](https://en.wikipedia.org/wiki/Pi), the ratio of a circle’s circumference to its diameter.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| result |
| --- |
| double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW PI()
```

| PI():double |
| --- |
| 3.141592653589793 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `POW` [esql-pow] 

**Syntax**

:::{image} images/pow.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`base`
:   Numeric expression for the base. If `null`, the function returns `null`.

`exponent`
:   Numeric expression for the exponent. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the value of `base` raised to the power of `exponent`.

::::{note} 
It is still possible to overflow a double result here; in that case, null will be returned.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| base | exponent | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| double | unsigned_long | double |
| integer | double | double |
| integer | integer | double |
| integer | long | double |
| integer | unsigned_long | double |
| long | double | double |
| long | integer | double |
| long | long | double |
| long | unsigned_long | double |
| unsigned_long | double | double |
| unsigned_long | integer | double |
| unsigned_long | long | double |
| unsigned_long | unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW base = 2.0, exponent = 2
| EVAL result = POW(base, exponent)
```

| base:double | exponent:integer | result:double |
| --- | --- | --- |
| 2.0 | 2 | 4.0 |

The exponent can be a fraction, which is similar to performing a root. For example, the exponent of `0.5` will give the square root of the base:

```esql
ROW base = 4, exponent = 0.5
| EVAL s = POW(base, exponent)
```

| base:integer | exponent:double | s:double |
| --- | --- | --- |
| 4 | 0.5 | 2.0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ROUND` [esql-round] 

**Syntax**

:::{image} images/round.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   The numeric value to round. If `null`, the function returns `null`.

`decimals`
:   The number of decimal places to round to. Defaults to 0. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Rounds a number to the specified number of decimal places. Defaults to 0, which returns the nearest integer. If the precision is a negative number, rounds to the number of digits left of the decimal point.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | decimals | result |
| --- | --- | --- |
| double | integer | double |
| double | long | double |
| double |  | double |
| integer | integer | integer |
| integer | long | integer |
| integer |  | integer |
| long | integer | long |
| long | long | long |
| long |  | long |
| unsigned_long | integer | unsigned_long |
| unsigned_long | long | unsigned_long |
| unsigned_long |  | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP first_name, last_name, height
| EVAL height_ft = ROUND(height * 3.281, 1)
```

| first_name:keyword | last_name:keyword | height:double | height_ft:double |
| --- | --- | --- | --- |
| Arumugam | Ossenbruggen | 2.1 | 6.9 |
| Kwee | Schusler | 2.1 | 6.9 |
| Saniya | Kalloufi | 2.1 | 6.9 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SIGNUM` [esql-signum] 

**Syntax**

:::{image} images/signum.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the sign of the given number. It returns `-1` for negative numbers, `0` for `0` and `1` for positive numbers.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW d = 100.0
| EVAL s = SIGNUM(d)
```

| d: double | s:double |
| --- | --- |
| 100 | 1.0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SIN` [esql-sin] 

**Syntax**

:::{image} images/sin.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`angle`
:   An angle, in radians. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [sine](https://en.wikipedia.org/wiki/Sine_and_cosine) of an angle.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| angle | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL sin=SIN(a)
```

| a:double | sin:double |
| --- | --- |
| 1.8 | 0.9738476308781951 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SINH` [esql-sinh] 

**Syntax**

:::{image} images/sinh.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [hyperbolic sine](https://en.wikipedia.org/wiki/Hyperbolic_functions) of a number.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL sinh=SINH(a)
```

| a:double | sinh:double |
| --- | --- |
| 1.8 | 2.94217428809568 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SQRT` [esql-sqrt] 

**Syntax**

:::{image} images/sqrt.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the square root of a number. The input can be any numeric value, the return value is always a double. Square roots of negative numbers and infinities are null.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW d = 100.0
| EVAL s = SQRT(d)
```

| d: double | s:double |
| --- | --- |
| 100.0 | 10.0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TAN` [esql-tan] 

**Syntax**

:::{image} images/tan.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`angle`
:   An angle, in radians. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [tangent](https://en.wikipedia.org/wiki/Sine_and_cosine) of an angle.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| angle | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL tan=TAN(a)
```

| a:double | tan:double |
| --- | --- |
| 1.8 | -4.286261674628062 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TANH` [esql-tanh] 

**Syntax**

:::{image} images/tanh.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Numeric expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_functions) of a number.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=1.8
| EVAL tanh=TANH(a)
```

| a:double | tanh:double |
| --- | --- |
| 1.8 | 0.9468060128462683 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TAU` [esql-tau] 

**Syntax**

:::{image} images/tau.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the [ratio](https://tauday.com/tau-manifesto) of a circle’s circumference to its radius.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| result |
| --- |
| double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW TAU()
```

| TAU():double |
| --- |
| 6.283185307179586 |


## {{esql}} Full-text search functions [esql-search-functions]


Full text functions are used to search for text in fields. [Text analysis](analysis.md) is used to analyze the query before it is searched.

Full text functions can be used to match [multivalued fields](esql-multivalued-fields.md). A multivalued field that contains a value that matches a full text query is considered to match the query.

Full text functions are significantly more performant for text search use cases on large data sets than using pattern matching or regular expressions with `LIKE` or `RLIKE`

See [full text search limitations](esql-limitations.md#esql-limitations-full-text-search) for information on the limitations of full text search.

{{esql}} supports these full-text search functions:

%  tag::search_list[]

* [preview] [`KQL`](esql-functions-operators.md#esql-kql)
* [preview] [`MATCH`](esql-functions-operators.md#esql-match)
* [preview] [`QSTR`](esql-functions-operators.md#esql-qstr)

%  end::search_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `KQL` [esql-kql] 

::::{warning} 
Do not use on production environments. This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


**Syntax**

:::{image} images/kql.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`query`
:   Query string in KQL query string format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Performs a KQL query. Returns true if the provided KQL query string matches the row.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| query | result |
| --- | --- |
| keyword | boolean |
| text | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM books
| WHERE KQL("author: Faulkner")
| KEEP book_no, author
| SORT book_no
| LIMIT 5
```

| book_no:keyword | author:text |
| --- | --- |
| 2378 | [Carol Faulkner, Holly Byers Ochoa, Lucretia Mott] |
| 2713 | William Faulkner |
| 2847 | Colleen Faulkner |
| 2883 | William Faulkner |
| 3293 | Danny Faulkner |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MATCH` [esql-match] 

::::{warning} 
Do not use on production environments. This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


**Syntax**

:::{image} images/match.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Field that the query will target.

`query`
:   Value to find in the provided field.

`options`
:   (Optional) Match additional options as [function named parameters](esql-syntax.md#esql-function-named-params). See [match query](query-dsl-match-query.md) for more information.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Use `MATCH` to perform a [match query](query-dsl-match-query.md) on the specified field. Using `MATCH` is equivalent to using the `match` query in the Elasticsearch Query DSL.  Match can be used on fields from the text family like [text](text.md) and [semantic_text](semantic-text.md), as well as other field types like keyword, boolean, dates, and numeric types.  Match can use [function named parameters](esql-syntax.md#esql-function-named-params) to specify additional options for the match query. All [match query parameters](query-dsl-match-query.md#match-field-params) are supported.  For a simplified syntax, you can use the [match operator](esql-functions-operators.md#esql-search-operators) `:` operator instead of `MATCH`.  `MATCH` returns true if the provided query matches the row.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | query | options | result |
| --- | --- | --- | --- |
| boolean | boolean | named parameters | boolean |
| boolean | keyword | named parameters | boolean |
| date | date | named parameters | boolean |
| date | keyword | named parameters | boolean |
| date_nanos | date_nanos | named parameters | boolean |
| date_nanos | keyword | named parameters | boolean |
| double | double | named parameters | boolean |
| double | integer | named parameters | boolean |
| double | keyword | named parameters | boolean |
| double | long | named parameters | boolean |
| integer | double | named parameters | boolean |
| integer | integer | named parameters | boolean |
| integer | keyword | named parameters | boolean |
| integer | long | named parameters | boolean |
| ip | ip | named parameters | boolean |
| ip | keyword | named parameters | boolean |
| keyword | keyword | named parameters | boolean |
| long | double | named parameters | boolean |
| long | integer | named parameters | boolean |
| long | keyword | named parameters | boolean |
| long | long | named parameters | boolean |
| text | keyword | named parameters | boolean |
| unsigned_long | double | named parameters | boolean |
| unsigned_long | integer | named parameters | boolean |
| unsigned_long | keyword | named parameters | boolean |
| unsigned_long | long | named parameters | boolean |
| unsigned_long | unsigned_long | named parameters | boolean |
| version | keyword | named parameters | boolean |
| version | version | named parameters | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported function named parameters**

| name | types | description |
| --- | --- | --- |
| fuzziness | [keyword] | Maximum edit distance allowed for matching. |
| auto_generate_synonyms_phrase_query | [boolean] | If true, match phrase queries are automatically created for multi-term synonyms. |
| analyzer | [keyword] | Analyzer used to convert the text in the query value into token. |
| minimum_should_match | [integer] | Minimum number of clauses that must match for a document to be returned. |
| zero_terms_query | [keyword] | Number of beginning characters left unchanged for fuzzy matching. |
| boost | [float] | Floating point number used to decrease or increase the relevance scores of the query. |
| fuzzy_transpositions | [boolean] | If true, edits for fuzzy matching include transpositions of two adjacent characters (ab → ba). |
| fuzzy_rewrite | [keyword] | Method used to rewrite the query. See the rewrite parameter for valid values and more information. |
| prefix_length | [integer] | Number of beginning characters left unchanged for fuzzy matching. |
| lenient | [boolean] | If false, format-based errors, such as providing a text query value for a numeric field, are returned. |
| operator | [keyword] | Boolean logic used to interpret text in the query value. |
| max_expansions | [integer] | Maximum number of terms to which the query will expand. |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
FROM books
| WHERE MATCH(author, "Faulkner")
| KEEP book_no, author
| SORT book_no
| LIMIT 5
```

| book_no:keyword | author:text |
| --- | --- |
| 2378 | [Carol Faulkner, Holly Byers Ochoa, Lucretia Mott] |
| 2713 | William Faulkner |
| 2847 | Colleen Faulkner |
| 2883 | William Faulkner |
| 3293 | Danny Faulkner |

```esql
FROM books
| WHERE MATCH(title, "Hobbit Back Again", {"operator": "AND"})
| KEEP title;
```

| title:text |
| --- |
| The Hobbit or There and Back Again |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `QSTR` [esql-qstr] 

::::{warning} 
Do not use on production environments. This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


**Syntax**

:::{image} images/qstr.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`query`
:   Query string in Lucene query string format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Performs a [query string query](query-dsl-query-string-query.md). Returns true if the provided query string matches the row.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| query | result |
| --- | --- |
| keyword | boolean |
| text | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM books
| WHERE QSTR("author: Faulkner")
| KEEP book_no, author
| SORT book_no
| LIMIT 5
```

| book_no:keyword | author:text |
| --- | --- |
| 2378 | [Carol Faulkner, Holly Byers Ochoa, Lucretia Mott] |
| 2713 | William Faulkner |
| 2847 | Colleen Faulkner |
| 2883 | William Faulkner |
| 3293 | Danny Faulkner |


## {{esql}} spatial functions [esql-spatial-functions]


{{esql}} supports these spatial functions:

%  tag::spatial_list[]

* [`ST_DISTANCE`](esql-functions-operators.md#esql-st_distance)
* [`ST_INTERSECTS`](esql-functions-operators.md#esql-st_intersects)
* [`ST_DISJOINT`](esql-functions-operators.md#esql-st_disjoint)
* [`ST_CONTAINS`](esql-functions-operators.md#esql-st_contains)
* [`ST_WITHIN`](esql-functions-operators.md#esql-st_within)
* [`ST_X`](esql-functions-operators.md#esql-st_x)
* [`ST_Y`](esql-functions-operators.md#esql-st_y)
* [preview] [`ST_ENVELOPE`](esql-functions-operators.md#esql-st_envelope)
* [preview] [`ST_XMAX`](esql-functions-operators.md#esql-st_xmax)
* [preview] [`ST_XMIN`](esql-functions-operators.md#esql-st_xmin)
* [preview] [`ST_YMAX`](esql-functions-operators.md#esql-st_ymax)
* [preview] [`ST_YMIN`](esql-functions-operators.md#esql-st_ymin)

%  end::spatial_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_DISTANCE` [esql-st_distance] 

**Syntax**

:::{image} images/st_distance.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`geomA`
:   Expression of type `geo_point` or `cartesian_point`. If `null`, the function returns `null`.

`geomB`
:   Expression of type `geo_point` or `cartesian_point`. If `null`, the function returns `null`. The second parameter must also have the same coordinate system as the first. This means it is not possible to combine `geo_point` and `cartesian_point` parameters.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Computes the distance between two points. For cartesian geometries, this is the pythagorean distance in the same units as the original coordinates. For geographic geometries, this is the circular distance along the great circle in meters.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| geomA | geomB | result |
| --- | --- | --- |
| cartesian_point | cartesian_point | double |
| geo_point | geo_point | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| WHERE abbrev == "CPH"
| EVAL distance = ST_DISTANCE(location, city_location)
| KEEP abbrev, name, location, city_location, distance
```

| abbrev:k | name:text | location:geo_point | city_location:geo_point | distance:d |
| --- | --- | --- | --- | --- |
| CPH | Copenhagen | POINT(12.6493508684508 55.6285017221528) | POINT(12.5683 55.6761) | 7339.573896618216 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_INTERSECTS` [esql-st_intersects] 

**Syntax**

:::{image} images/st_intersects.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`geomA`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`.

`geomB`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`. The second parameter must also have the same coordinate system as the first. This means it is not possible to combine `geo_*` and `cartesian_*` parameters.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns true if two geometries intersect. They intersect if they have any point in common, including their interior points (points along lines or within polygons). This is the inverse of the [ST_DISJOINT](esql-functions-operators.md#esql-st_disjoint) function. In mathematical terms: ST_Intersects(A, B) ⇔ A ⋂ B ≠ ∅

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| geomA | geomB | result |
| --- | --- | --- |
| cartesian_point | cartesian_point | boolean |
| cartesian_point | cartesian_shape | boolean |
| cartesian_shape | cartesian_point | boolean |
| cartesian_shape | cartesian_shape | boolean |
| geo_point | geo_point | boolean |
| geo_point | geo_shape | boolean |
| geo_shape | geo_point | boolean |
| geo_shape | geo_shape | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| WHERE ST_INTERSECTS(location, TO_GEOSHAPE("POLYGON((42 14, 43 14, 43 15, 42 15, 42 14))"))
```

| abbrev:keyword | city:keyword | city_location:geo_point | country:keyword | location:geo_point | name:text | scalerank:i | type:k |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HOD | Al Ḩudaydah | POINT(42.9511 14.8022) | Yemen | POINT(42.97109630194 14.7552534413725) | Hodeidah Int’l | 9 | mid |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_DISJOINT` [esql-st_disjoint] 

**Syntax**

:::{image} images/st_disjoint.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`geomA`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`.

`geomB`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`. The second parameter must also have the same coordinate system as the first. This means it is not possible to combine `geo_*` and `cartesian_*` parameters.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns whether the two geometries or geometry columns are disjoint. This is the inverse of the [ST_INTERSECTS](esql-functions-operators.md#esql-st_intersects) function. In mathematical terms: ST_Disjoint(A, B) ⇔ A ⋂ B = ∅

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| geomA | geomB | result |
| --- | --- | --- |
| cartesian_point | cartesian_point | boolean |
| cartesian_point | cartesian_shape | boolean |
| cartesian_shape | cartesian_point | boolean |
| cartesian_shape | cartesian_shape | boolean |
| geo_point | geo_point | boolean |
| geo_point | geo_shape | boolean |
| geo_shape | geo_point | boolean |
| geo_shape | geo_shape | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE ST_DISJOINT(city_boundary, TO_GEOSHAPE("POLYGON((-10 -60, 120 -60, 120 60, -10 60, -10 -60))"))
| KEEP abbrev, airport, region, city, city_location
```

| abbrev:keyword | airport:text | region:text | city:keyword | city_location:geo_point |
| --- | --- | --- | --- | --- |
| ACA | General Juan N Alvarez Int’l | Acapulco de Juárez | Acapulco de Juárez | POINT (-99.8825 16.8636) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_CONTAINS` [esql-st_contains] 

**Syntax**

:::{image} images/st_contains.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`geomA`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`.

`geomB`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`. The second parameter must also have the same coordinate system as the first. This means it is not possible to combine `geo_*` and `cartesian_*` parameters.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns whether the first geometry contains the second geometry. This is the inverse of the [ST_WITHIN](esql-functions-operators.md#esql-st_within) function.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| geomA | geomB | result |
| --- | --- | --- |
| cartesian_point | cartesian_point | boolean |
| cartesian_point | cartesian_shape | boolean |
| cartesian_shape | cartesian_point | boolean |
| cartesian_shape | cartesian_shape | boolean |
| geo_point | geo_point | boolean |
| geo_point | geo_shape | boolean |
| geo_shape | geo_point | boolean |
| geo_shape | geo_shape | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE ST_CONTAINS(city_boundary, TO_GEOSHAPE("POLYGON((109.35 18.3, 109.45 18.3, 109.45 18.4, 109.35 18.4, 109.35 18.3))"))
| KEEP abbrev, airport, region, city, city_location
```

| abbrev:keyword | airport:text | region:text | city:keyword | city_location:geo_point |
| --- | --- | --- | --- | --- |
| SYX | Sanya Phoenix Int’l | 天涯区 | Sanya | POINT(109.5036 18.2533) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_WITHIN` [esql-st_within] 

**Syntax**

:::{image} images/st_within.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`geomA`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`.

`geomB`
:   Expression of type `geo_point`, `cartesian_point`, `geo_shape` or `cartesian_shape`. If `null`, the function returns `null`. The second parameter must also have the same coordinate system as the first. This means it is not possible to combine `geo_*` and `cartesian_*` parameters.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns whether the first geometry is within the second geometry. This is the inverse of the [ST_CONTAINS](esql-functions-operators.md#esql-st_contains) function.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| geomA | geomB | result |
| --- | --- | --- |
| cartesian_point | cartesian_point | boolean |
| cartesian_point | cartesian_shape | boolean |
| cartesian_shape | cartesian_point | boolean |
| cartesian_shape | cartesian_shape | boolean |
| geo_point | geo_point | boolean |
| geo_point | geo_shape | boolean |
| geo_shape | geo_point | boolean |
| geo_shape | geo_shape | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE ST_WITHIN(city_boundary, TO_GEOSHAPE("POLYGON((109.1 18.15, 109.6 18.15, 109.6 18.65, 109.1 18.65, 109.1 18.15))"))
| KEEP abbrev, airport, region, city, city_location
```

| abbrev:keyword | airport:text | region:text | city:keyword | city_location:geo_point |
| --- | --- | --- | --- | --- |
| SYX | Sanya Phoenix Int’l | 天涯区 | Sanya | POINT(109.5036 18.2533) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_X` [esql-st_x] 

**Syntax**

:::{image} images/st_x.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`point`
:   Expression of type `geo_point` or `cartesian_point`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts the `x` coordinate from the supplied point. If the points is of type `geo_point` this is equivalent to extracting the `longitude` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| point | result |
| --- | --- |
| cartesian_point | double |
| geo_point | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW point = TO_GEOPOINT("POINT(42.97109629958868 14.7552534006536)")
| EVAL x =  ST_X(point), y = ST_Y(point)
```

| point:geo_point | x:double | y:double |
| --- | --- | --- |
| POINT(42.97109629958868 14.7552534006536) | 42.97109629958868 | 14.7552534006536 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_Y` [esql-st_y] 

**Syntax**

:::{image} images/st_y.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`point`
:   Expression of type `geo_point` or `cartesian_point`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts the `y` coordinate from the supplied point. If the points is of type `geo_point` this is equivalent to extracting the `latitude` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| point | result |
| --- | --- |
| cartesian_point | double |
| geo_point | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW point = TO_GEOPOINT("POINT(42.97109629958868 14.7552534006536)")
| EVAL x =  ST_X(point), y = ST_Y(point)
```

| point:geo_point | x:double | y:double |
| --- | --- | --- |
| POINT(42.97109629958868 14.7552534006536) | 42.97109629958868 | 14.7552534006536 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_ENVELOPE` [esql-st_envelope] 

**Syntax**

:::{image} images/st_envelope.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`geometry`
:   Expression of type `geo_point`, `geo_shape`, `cartesian_point` or `cartesian_shape`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Determines the minimum bounding box of the supplied geometry.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| geometry | result |
| --- | --- |
| cartesian_point | cartesian_shape |
| cartesian_shape | cartesian_shape |
| geo_point | geo_shape |
| geo_shape | geo_shape |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE abbrev == "CPH"
| EVAL envelope = ST_ENVELOPE(city_boundary)
| KEEP abbrev, airport, envelope
```

| abbrev:keyword | airport:text | envelope:geo_shape |
| --- | --- | --- |
| CPH | Copenhagen | BBOX(12.453, 12.6398, 55.7327, 55.6318) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_XMAX` [esql-st_xmax] 

**Syntax**

:::{image} images/st_xmax.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`point`
:   Expression of type `geo_point`, `geo_shape`, `cartesian_point` or `cartesian_shape`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts the maximum value of the `x` coordinates from the supplied geometry. If the geometry is of type `geo_point` or `geo_shape` this is equivalent to extracting the maximum `longitude` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| point | result |
| --- | --- |
| cartesian_point | double |
| cartesian_shape | double |
| geo_point | double |
| geo_shape | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE abbrev == "CPH"
| EVAL envelope = ST_ENVELOPE(city_boundary)
| EVAL xmin = ST_XMIN(envelope), xmax = ST_XMAX(envelope), ymin = ST_YMIN(envelope), ymax = ST_YMAX(envelope)
| KEEP abbrev, airport, xmin, xmax, ymin, ymax
```

| abbrev:keyword | airport:text | xmin:double | xmax:double | ymin:double | ymax:double |
| --- | --- | --- | --- | --- | --- |
| CPH | Copenhagen | 12.453 | 12.6398 | 55.6318 | 55.7327 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_XMIN` [esql-st_xmin] 

**Syntax**

:::{image} images/st_xmin.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`point`
:   Expression of type `geo_point`, `geo_shape`, `cartesian_point` or `cartesian_shape`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts the minimum value of the `x` coordinates from the supplied geometry. If the geometry is of type `geo_point` or `geo_shape` this is equivalent to extracting the minimum `longitude` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| point | result |
| --- | --- |
| cartesian_point | double |
| cartesian_shape | double |
| geo_point | double |
| geo_shape | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE abbrev == "CPH"
| EVAL envelope = ST_ENVELOPE(city_boundary)
| EVAL xmin = ST_XMIN(envelope), xmax = ST_XMAX(envelope), ymin = ST_YMIN(envelope), ymax = ST_YMAX(envelope)
| KEEP abbrev, airport, xmin, xmax, ymin, ymax
```

| abbrev:keyword | airport:text | xmin:double | xmax:double | ymin:double | ymax:double |
| --- | --- | --- | --- | --- | --- |
| CPH | Copenhagen | 12.453 | 12.6398 | 55.6318 | 55.7327 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_YMAX` [esql-st_ymax] 

**Syntax**

:::{image} images/st_ymax.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`point`
:   Expression of type `geo_point`, `geo_shape`, `cartesian_point` or `cartesian_shape`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts the maximum value of the `y` coordinates from the supplied geometry. If the geometry is of type `geo_point` or `geo_shape` this is equivalent to extracting the maximum `latitude` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| point | result |
| --- | --- |
| cartesian_point | double |
| cartesian_shape | double |
| geo_point | double |
| geo_shape | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE abbrev == "CPH"
| EVAL envelope = ST_ENVELOPE(city_boundary)
| EVAL xmin = ST_XMIN(envelope), xmax = ST_XMAX(envelope), ymin = ST_YMIN(envelope), ymax = ST_YMAX(envelope)
| KEEP abbrev, airport, xmin, xmax, ymin, ymax
```

| abbrev:keyword | airport:text | xmin:double | xmax:double | ymin:double | ymax:double |
| --- | --- | --- | --- | --- | --- |
| CPH | Copenhagen | 12.453 | 12.6398 | 55.6318 | 55.7327 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ST_YMIN` [esql-st_ymin] 

**Syntax**

:::{image} images/st_ymin.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`point`
:   Expression of type `geo_point`, `geo_shape`, `cartesian_point` or `cartesian_shape`. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Extracts the minimum value of the `y` coordinates from the supplied geometry. If the geometry is of type `geo_point` or `geo_shape` this is equivalent to extracting the minimum `latitude` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| point | result |
| --- | --- |
| cartesian_point | double |
| cartesian_shape | double |
| geo_point | double |
| geo_shape | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airport_city_boundaries
| WHERE abbrev == "CPH"
| EVAL envelope = ST_ENVELOPE(city_boundary)
| EVAL xmin = ST_XMIN(envelope), xmax = ST_XMAX(envelope), ymin = ST_YMIN(envelope), ymax = ST_YMAX(envelope)
| KEEP abbrev, airport, xmin, xmax, ymin, ymax
```

| abbrev:keyword | airport:text | xmin:double | xmax:double | ymin:double | ymax:double |
| --- | --- | --- | --- | --- | --- |
| CPH | Copenhagen | 12.453 | 12.6398 | 55.6318 | 55.7327 |


## {{esql}} string functions [esql-string-functions]


{{esql}} supports these string functions:

%  tag::string_list[]

* [`BIT_LENGTH`](esql-functions-operators.md#esql-bit_length)
* [`BYTE_LENGTH`](esql-functions-operators.md#esql-byte_length)
* [`CONCAT`](esql-functions-operators.md#esql-concat)
* [`ENDS_WITH`](esql-functions-operators.md#esql-ends_with)
* [`FROM_BASE64`](esql-functions-operators.md#esql-from_base64)
* [`HASH`](esql-functions-operators.md#esql-hash)
* [`LEFT`](esql-functions-operators.md#esql-left)
* [`LENGTH`](esql-functions-operators.md#esql-length)
* [`LOCATE`](esql-functions-operators.md#esql-locate)
* [`LTRIM`](esql-functions-operators.md#esql-ltrim)
* [`MD5`](esql-functions-operators.md#esql-md5)
* [`REPEAT`](esql-functions-operators.md#esql-repeat)
* [`REPLACE`](esql-functions-operators.md#esql-replace)
* [`REVERSE`](esql-functions-operators.md#esql-reverse)
* [`RIGHT`](esql-functions-operators.md#esql-right)
* [`RTRIM`](esql-functions-operators.md#esql-rtrim)
* [`SHA1`](esql-functions-operators.md#esql-sha1)
* [`SHA256`](esql-functions-operators.md#esql-sha256)
* [`SPACE`](esql-functions-operators.md#esql-space)
* [`SPLIT`](esql-functions-operators.md#esql-split)
* [`STARTS_WITH`](esql-functions-operators.md#esql-starts_with)
* [`SUBSTRING`](esql-functions-operators.md#esql-substring)
* [`TO_BASE64`](esql-functions-operators.md#esql-to_base64)
* [`TO_LOWER`](esql-functions-operators.md#esql-to_lower)
* [`TO_UPPER`](esql-functions-operators.md#esql-to_upper)
* [`TRIM`](esql-functions-operators.md#esql-trim)

%  end::string_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `BIT_LENGTH` [esql-bit_length] 

**Syntax**

:::{image} images/bit_length.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the bit length of a string.

::::{note} 
All strings are in UTF-8, so a single character can use multiple bytes.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | integer |
| text | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| WHERE country == "India"
| KEEP city
| EVAL fn_length = LENGTH(city), fn_bit_length = BIT_LENGTH(city)
```

| city:keyword | fn_length:integer | fn_bit_length:integer |
| --- | --- | --- |
| Agwār | 5 | 48 |
| Ahmedabad | 9 | 72 |
| Bangalore | 9 | 72 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `BYTE_LENGTH` [esql-byte_length] 

**Syntax**

:::{image} images/byte_length.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the byte length of a string.

::::{note} 
All strings are in UTF-8, so a single character can use multiple bytes.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | integer |
| text | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| WHERE country == "India"
| KEEP city
| EVAL fn_length = LENGTH(city), fn_byte_length = BYTE_LENGTH(city)
```

| city:keyword | fn_length:integer | fn_byte_length:integer |
| --- | --- | --- |
| Agwār | 5 | 6 |
| Ahmedabad | 9 | 9 |
| Bangalore | 9 | 9 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `CONCAT` [esql-concat] 

**Syntax**

:::{image} images/concat.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string1`
:   Strings to concatenate.

`string2`
:   Strings to concatenate.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Concatenates two or more strings.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string1 | string2 | result |
| --- | --- | --- |
| keyword | keyword | keyword |
| keyword | text | keyword |
| text | keyword | keyword |
| text | text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP first_name, last_name
| EVAL fullname = CONCAT(first_name, " ", last_name)
```

| first_name:keyword | last_name:keyword | fullname:keyword |
| --- | --- | --- |
| Alejandro | McAlpine | Alejandro McAlpine |
| Amabile | Gomatam | Amabile Gomatam |
| Anneke | Preusig | Anneke Preusig |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `ENDS_WITH` [esql-ends_with] 

**Syntax**

:::{image} images/ends_with.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`str`
:   String expression. If `null`, the function returns `null`.

`suffix`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a boolean that indicates whether a keyword string ends with another string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | suffix | result |
| --- | --- | --- |
| keyword | keyword | boolean |
| keyword | text | boolean |
| text | keyword | boolean |
| text | text | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP last_name
| EVAL ln_E = ENDS_WITH(last_name, "d")
```

| last_name:keyword | ln_E:boolean |
| --- | --- |
| Awdeh | false |
| Azuma | false |
| Baek | false |
| Bamford | true |
| Bernatsky | false |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `FROM_BASE64` [esql-from_base64] 

**Syntax**

:::{image} images/from_base64.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   A base64 string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Decode a base64 string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
row a = "ZWxhc3RpYw=="
| eval d = from_base64(a)
```

| a:keyword | d:keyword |
| --- | --- |
| ZWxhc3RpYw== | elastic |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `HASH` [esql-hash] 

**Syntax**

:::{image} images/hash.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`algorithm`
:   Hash algorithm to use.

`input`
:   Input to hash.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Computes the hash of the input using various algorithms such as MD5, SHA, SHA-224, SHA-256, SHA-384, SHA-512.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| algorithm | input | result |
| --- | --- | --- |
| keyword | keyword | keyword |
| keyword | text | keyword |
| text | keyword | keyword |
| text | text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM sample_data
| WHERE message != "Connection error"
| EVAL md5 = hash("md5", message), sha256 = hash("sha256", message)
| KEEP message, md5, sha256;
```

| message:keyword | md5:keyword | sha256:keyword |
| --- | --- | --- |
| Connected to 10.1.0.1 | abd7d1ce2bb636842a29246b3512dcae | 6d8372129ad78770f7185554dd39864749a62690216460752d6c075fa38ad85c |
| Connected to 10.1.0.2 | 8f8f1cb60832d153f5b9ec6dc828b93f | b0db24720f15857091b3c99f4c4833586d0ea3229911b8777efb8d917cf27e9a |
| Connected to 10.1.0.3 | 912b6dc13503165a15de43304bb77c78 | 75b0480188db8acc4d5cc666a51227eb2bc5b989cd8ca912609f33e0846eff57 |
| Disconnected | ef70e46fd3bbc21e3e1f0b6815e750c0 | 04dfac3671b494ad53fcd152f7a14511bfb35747278aad8ce254a0d6e4ba4718 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LEFT` [esql-left] 

**Syntax**

:::{image} images/left.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   The string from which to return a substring.

`length`
:   The number of characters to return.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the substring that extracts *length* chars from *string* starting from the left.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | length | result |
| --- | --- | --- |
| keyword | integer | keyword |
| text | integer | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP last_name
| EVAL left = LEFT(last_name, 3)
| SORT last_name ASC
| LIMIT 5
```

| last_name:keyword | left:keyword |
| --- | --- |
| Awdeh | Awd |
| Azuma | Azu |
| Baek | Bae |
| Bamford | Bam |
| Bernatsky | Ber |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LENGTH` [esql-length] 

**Syntax**

:::{image} images/length.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns the character length of a string.

::::{note} 
All strings are in UTF-8, so a single character can use multiple bytes.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | integer |
| text | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM airports
| WHERE country == "India"
| KEEP city
| EVAL fn_length = LENGTH(city)
```

| city:keyword | fn_length:integer |
| --- | --- |
| Agwār | 5 |
| Ahmedabad | 9 |
| Bangalore | 9 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LOCATE` [esql-locate] 

**Syntax**

:::{image} images/locate.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   An input string

`substring`
:   A substring to locate in the input string

`start`
:   The start index

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns an integer that indicates the position of a keyword substring within another string. Returns `0` if the substring cannot be found. Note that string positions start from `1`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | substring | start | result |
| --- | --- | --- | --- |
| keyword | keyword | integer | integer |
| keyword | keyword |  | integer |
| keyword | text | integer | integer |
| keyword | text |  | integer |
| text | keyword | integer | integer |
| text | keyword |  | integer |
| text | text | integer | integer |
| text | text |  | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
row a = "hello"
| eval a_ll = locate(a, "ll")
```

| a:keyword | a_ll:integer |
| --- | --- |
| hello | 3 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `LTRIM` [esql-ltrim] 

**Syntax**

:::{image} images/ltrim.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Removes leading whitespaces from a string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW message = "   some text  ",  color = " red "
| EVAL message = LTRIM(message)
| EVAL color = LTRIM(color)
| EVAL message = CONCAT("'", message, "'")
| EVAL color = CONCAT("'", color, "'")
```

| message:keyword | color:keyword |
| --- | --- |
| 'some text  ' | 'red ' |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MD5` [esql-md5] 

**Syntax**

:::{image} images/md5.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`input`
:   Input to hash.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Computes the MD5 hash of the input.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| input | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM sample_data
| WHERE message != "Connection error"
| EVAL md5 = md5(message)
| KEEP message, md5;
```

| message:keyword | md5:keyword |
| --- | --- |
| Connected to 10.1.0.1 | abd7d1ce2bb636842a29246b3512dcae |
| Connected to 10.1.0.2 | 8f8f1cb60832d153f5b9ec6dc828b93f |
| Connected to 10.1.0.3 | 912b6dc13503165a15de43304bb77c78 |
| Disconnected | ef70e46fd3bbc21e3e1f0b6815e750c0 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `REPEAT` [esql-repeat] 

**Syntax**

:::{image} images/repeat.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression.

`number`
:   Number times to repeat.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a string constructed by concatenating `string` with itself the specified `number` of times.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | number | result |
| --- | --- | --- |
| keyword | integer | keyword |
| text | integer | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = "Hello!"
| EVAL triple_a = REPEAT(a, 3)
```

| a:keyword | triple_a:keyword |
| --- | --- |
| Hello! | Hello!Hello!Hello! |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `REPLACE` [esql-replace] 

**Syntax**

:::{image} images/replace.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression.

`regex`
:   Regular expression.

`newString`
:   Replacement string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

The function substitutes in the string `str` any match of the regular expression `regex` with the replacement string `newStr`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | regex | newString | result |
| --- | --- | --- | --- |
| keyword | keyword | keyword | keyword |
| keyword | keyword | text | keyword |
| keyword | text | keyword | keyword |
| keyword | text | text | keyword |
| text | keyword | keyword | keyword |
| text | keyword | text | keyword |
| text | text | keyword | keyword |
| text | text | text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

This example replaces any occurrence of the word "World" with the word "Universe":

```esql
ROW str = "Hello World"
| EVAL str = REPLACE(str, "World", "Universe")
| KEEP str
```

| str:keyword |
| --- |
| Hello Universe |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `REVERSE` [esql-reverse] 

**Syntax**

:::{image} images/reverse.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`str`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a new string representing the input string in reverse order.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW message = "Some Text" | EVAL message_reversed = REVERSE(message);
```

| message:keyword | message_reversed:keyword |
| --- | --- |
| Some Text | txeT emoS |

`REVERSE` works with unicode, too! It keeps unicode grapheme clusters together during reversal.

```esql
ROW bending_arts = "💧🪨🔥💨" | EVAL bending_arts_reversed = REVERSE(bending_arts);
```

| bending_arts:keyword | bending_arts_reversed:keyword |
| --- | --- |
| 💧🪨🔥💨 | 💨🔥🪨💧 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `RIGHT` [esql-right] 

**Syntax**

:::{image} images/right.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   The string from which to returns a substring.

`length`
:   The number of characters to return.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Return the substring that extracts *length* chars from *str* starting from the right.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | length | result |
| --- | --- | --- |
| keyword | integer | keyword |
| text | integer | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP last_name
| EVAL right = RIGHT(last_name, 3)
| SORT last_name ASC
| LIMIT 5
```

| last_name:keyword | right:keyword |
| --- | --- |
| Awdeh | deh |
| Azuma | uma |
| Baek | aek |
| Bamford | ord |
| Bernatsky | sky |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `RTRIM` [esql-rtrim] 

**Syntax**

:::{image} images/rtrim.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Removes trailing whitespaces from a string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW message = "   some text  ",  color = " red "
| EVAL message = RTRIM(message)
| EVAL color = RTRIM(color)
| EVAL message = CONCAT("'", message, "'")
| EVAL color = CONCAT("'", color, "'")
```

| message:keyword | color:keyword |
| --- | --- |
| '   some text' | ' red' |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SHA1` [esql-sha1] 

**Syntax**

:::{image} images/sha1.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`input`
:   Input to hash.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Computes the SHA1 hash of the input.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| input | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM sample_data
| WHERE message != "Connection error"
| EVAL sha1 = sha1(message)
| KEEP message, sha1;
```

| message:keyword | sha1:keyword |
| --- | --- |
| Connected to 10.1.0.1 | 42b85531a79088036a17759db7d2de292b92f57f |
| Connected to 10.1.0.2 | d30db445da2e9237c9718d0c7e4fb7cbbe9c2cb4 |
| Connected to 10.1.0.3 | 2733848d943809f0b10cad3e980763e88afb9853 |
| Disconnected | 771e05f27b99fd59f638f41a7a4e977b1d4691fe |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SHA256` [esql-sha256] 

**Syntax**

:::{image} images/sha256.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`input`
:   Input to hash.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Computes the SHA256 hash of the input.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| input | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM sample_data
| WHERE message != "Connection error"
| EVAL sha256 = sha256(message)
| KEEP message, sha256;
```

| message:keyword | sha256:keyword |
| --- | --- |
| Connected to 10.1.0.1 | 6d8372129ad78770f7185554dd39864749a62690216460752d6c075fa38ad85c |
| Connected to 10.1.0.2 | b0db24720f15857091b3c99f4c4833586d0ea3229911b8777efb8d917cf27e9a |
| Connected to 10.1.0.3 | 75b0480188db8acc4d5cc666a51227eb2bc5b989cd8ca912609f33e0846eff57 |
| Disconnected | 04dfac3671b494ad53fcd152f7a14511bfb35747278aad8ce254a0d6e4ba4718 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SPACE` [esql-space] 

**Syntax**

:::{image} images/space.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Number of spaces in result.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a string made of `number` spaces.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| integer | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW message = CONCAT("Hello", SPACE(1), "World!");
```

| message:keyword |
| --- |
| Hello World! |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SPLIT` [esql-split] 

**Syntax**

:::{image} images/split.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

`delim`
:   Delimiter. Only single byte delimiters are currently supported.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Split a single valued string into multiple strings.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | delim | result |
| --- | --- | --- |
| keyword | keyword | keyword |
| keyword | text | keyword |
| text | keyword | keyword |
| text | text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW words="foo;bar;baz;qux;quux;corge"
| EVAL word = SPLIT(words, ";")
```

| words:keyword | word:keyword |
| --- | --- |
| foo;bar;baz;qux;quux;corge | [foo,bar,baz,qux,quux,corge] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `STARTS_WITH` [esql-starts_with] 

**Syntax**

:::{image} images/starts_with.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`str`
:   String expression. If `null`, the function returns `null`.

`prefix`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a boolean that indicates whether a keyword string starts with another string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | prefix | result |
| --- | --- | --- |
| keyword | keyword | boolean |
| keyword | text | boolean |
| text | keyword | boolean |
| text | text | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
FROM employees
| KEEP last_name
| EVAL ln_S = STARTS_WITH(last_name, "B")
```

| last_name:keyword | ln_S:boolean |
| --- | --- |
| Awdeh | false |
| Azuma | false |
| Baek | true |
| Bamford | true |
| Bernatsky | true |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `SUBSTRING` [esql-substring] 

**Syntax**

:::{image} images/substring.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

`start`
:   Start position.

`length`
:   Length of the substring from the start position. Optional; if omitted, all positions after `start` are returned.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a substring of a string, specified by a start position and an optional length.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | start | length | result |
| --- | --- | --- | --- |
| keyword | integer | integer | keyword |
| text | integer | integer | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

This example returns the first three characters of every last name:

```esql
FROM employees
| KEEP last_name
| EVAL ln_sub = SUBSTRING(last_name, 1, 3)
```

| last_name:keyword | ln_sub:keyword |
| --- | --- |
| Awdeh | Awd |
| Azuma | Azu |
| Baek | Bae |
| Bamford | Bam |
| Bernatsky | Ber |

A negative start position is interpreted as being relative to the end of the string. This example returns the last three characters of of every last name:

```esql
FROM employees
| KEEP last_name
| EVAL ln_sub = SUBSTRING(last_name, -3, 3)
```

| last_name:keyword | ln_sub:keyword |
| --- | --- |
| Awdeh | deh |
| Azuma | uma |
| Baek | aek |
| Bamford | ord |
| Bernatsky | sky |

If length is omitted, substring returns the remainder of the string. This example returns all characters except for the first:

```esql
FROM employees
| KEEP last_name
| EVAL ln_sub = SUBSTRING(last_name, 2)
```

| last_name:keyword | ln_sub:keyword |
| --- | --- |
| Awdeh | wdeh |
| Azuma | zuma |
| Baek | aek |
| Bamford | amford |
| Bernatsky | ernatsky |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_BASE64` [esql-to_base64] 

**Syntax**

:::{image} images/to_base64.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   A string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Encode a string to a base64 string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
row a = "elastic"
| eval e = to_base64(a)
```

| a:keyword | e:keyword |
| --- | --- |
| elastic | ZWxhc3RpYw== |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_LOWER` [esql-to_lower] 

**Syntax**

:::{image} images/to_lower.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`str`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a new string representing the input string converted to lower case.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW message = "Some Text"
| EVAL message_lower = TO_LOWER(message)
```

| message:keyword | message_lower:keyword |
| --- | --- |
| Some Text | some text |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_UPPER` [esql-to_upper] 

**Syntax**

:::{image} images/to_upper.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`str`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a new string representing the input string converted to upper case.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW message = "Some Text"
| EVAL message_upper = TO_UPPER(message)
```

| message:keyword | message_upper:keyword |
| --- | --- |
| Some Text | SOME TEXT |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TRIM` [esql-trim] 

**Syntax**

:::{image} images/trim.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   String expression. If `null`, the function returns `null`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Removes leading and trailing whitespaces from a string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | result |
| --- | --- |
| keyword | keyword |
| text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW message = "   some text  ",  color = " red "
| EVAL message = TRIM(message)
| EVAL color = TRIM(color)
```

| message:s | color:s |
| --- | --- |
| some text | red |


## {{esql}} type conversion functions [esql-type-conversion-functions]


::::{tip} 
{{esql}} supports implicit casting from string literals to certain data types. Refer to [implicit casting](esql-implicit-casting.md) for details.

::::


{{esql}} supports these type conversion functions:

%  tag::type_list[]

* [`TO_BOOLEAN`](esql-functions-operators.md#esql-to_boolean)
* [`TO_CARTESIANPOINT`](esql-functions-operators.md#esql-to_cartesianpoint)
* [`TO_CARTESIANSHAPE`](esql-functions-operators.md#esql-to_cartesianshape)
* [preview] [`TO_DATEPERIOD`](esql-functions-operators.md#esql-to_dateperiod)
* [`TO_DATETIME`](esql-functions-operators.md#esql-to_datetime)
* [`TO_DATE_NANOS`](esql-functions-operators.md#esql-to_date_nanos)
* [`TO_DEGREES`](esql-functions-operators.md#esql-to_degrees)
* [`TO_DOUBLE`](esql-functions-operators.md#esql-to_double)
* [`TO_GEOPOINT`](esql-functions-operators.md#esql-to_geopoint)
* [`TO_GEOSHAPE`](esql-functions-operators.md#esql-to_geoshape)
* [`TO_INTEGER`](esql-functions-operators.md#esql-to_integer)
* [`TO_IP`](esql-functions-operators.md#esql-to_ip)
* [`TO_LONG`](esql-functions-operators.md#esql-to_long)
* [`TO_RADIANS`](esql-functions-operators.md#esql-to_radians)
* [`TO_STRING`](esql-functions-operators.md#esql-to_string)
* [preview] [`TO_TIMEDURATION`](esql-functions-operators.md#esql-to_timeduration)
* [preview] [`TO_UNSIGNED_LONG`](esql-functions-operators.md#esql-to_unsigned_long)
* [`TO_VERSION`](esql-functions-operators.md#esql-to_version)

%  end::type_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_BOOLEAN` [esql-to_boolean] 

**Syntax**

:::{image} images/to_boolean.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a boolean value. A string value of **true** will be case-insensitive converted to the Boolean **true**. For anything else, including the empty string, the function will return **false**. The numerical value of **0** will be converted to **false**, anything else will be converted to **true**.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| double | boolean |
| integer | boolean |
| keyword | boolean |
| long | boolean |
| text | boolean |
| unsigned_long | boolean |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW str = ["true", "TRuE", "false", "", "yes", "1"]
| EVAL bool = TO_BOOLEAN(str)
```

| str:keyword | bool:boolean |
| --- | --- |
| ["true", "TRuE", "false", "", "yes", "1"] | [true, true, false, false, false, false] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_CARTESIANPOINT` [esql-to_cartesianpoint] 

**Syntax**

:::{image} images/to_cartesianpoint.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a `cartesian_point` value. A string will only be successfully converted if it respects the [WKT Point](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| cartesian_point | cartesian_point |
| keyword | cartesian_point |
| text | cartesian_point |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW wkt = ["POINT(4297.11 -1475.53)", "POINT(7580.93 2272.77)"]
| MV_EXPAND wkt
| EVAL pt = TO_CARTESIANPOINT(wkt)
```

| wkt:keyword | pt:cartesian_point |
| --- | --- |
| "POINT(4297.11 -1475.53)" | POINT(4297.11 -1475.53) |
| "POINT(7580.93 2272.77)" | POINT(7580.93 2272.77) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_CARTESIANSHAPE` [esql-to_cartesianshape] 

**Syntax**

:::{image} images/to_cartesianshape.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a `cartesian_shape` value. A string will only be successfully converted if it respects the [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| cartesian_point | cartesian_shape |
| cartesian_shape | cartesian_shape |
| keyword | cartesian_shape |
| text | cartesian_shape |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW wkt = ["POINT(4297.11 -1475.53)", "POLYGON ((3339584.72 1118889.97, 4452779.63 4865942.27, 2226389.81 4865942.27, 1113194.90 2273030.92, 3339584.72 1118889.97))"]
| MV_EXPAND wkt
| EVAL geom = TO_CARTESIANSHAPE(wkt)
```

| wkt:keyword | geom:cartesian_shape |
| --- | --- |
| "POINT(4297.11 -1475.53)" | POINT(4297.11 -1475.53) |
| "POLYGON 3339584.72 1118889.97, 4452779.63 4865942.27, 2226389.81 4865942.27, 1113194.90 2273030.92, 3339584.72 1118889.97" | POLYGON 3339584.72 1118889.97, 4452779.63 4865942.27, 2226389.81 4865942.27, 1113194.90 2273030.92, 3339584.72 1118889.97 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_DATEPERIOD` [esql-to_dateperiod] 

**Syntax**

:::{image} images/to_dateperiod.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input is a valid constant date period expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value into a `date_period` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| date_period | date_period |
| keyword | date_period |
| text | date_period |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
row x = "2024-01-01"::datetime | eval y = x + "3 DAYS"::date_period, z = x - to_dateperiod("3 days");
```

| x:datetime | y:datetime | z:datetime |
| --- | --- | --- |
| 2024-01-01 | 2024-01-04 | 2023-12-29 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_DATETIME` [esql-to_datetime] 

**Syntax**

:::{image} images/to_datetime.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a date value. A string will only be successfully converted if it’s respecting the format `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`. To convert dates in other formats, use [`DATE_PARSE`](esql-functions-operators.md#esql-date_parse).

::::{note} 
Note that when converting from nanosecond resolution to millisecond resolution with this function, the nanosecond date is truncated, not rounded.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| date | date |
| date_nanos | date |
| double | date |
| integer | date |
| keyword | date |
| long | date |
| text | date |
| unsigned_long | date |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW string = ["1953-09-02T00:00:00.000Z", "1964-06-02T00:00:00.000Z", "1964-06-02 00:00:00"]
| EVAL datetime = TO_DATETIME(string)
```

| string:keyword | datetime:date |
| --- | --- |
| ["1953-09-02T00:00:00.000Z", "1964-06-02T00:00:00.000Z", "1964-06-02 00:00:00"] | [1953-09-02T00:00:00.000Z, 1964-06-02T00:00:00.000Z] |

Note that in this example, the last value in the source multi-valued field has not been converted. The reason being that if the date format is not respected, the conversion will result in a **null** value. When this happens a *Warning* header is added to the response. The header will provide information on the source of the failure:

`"Line 1:112: evaluation of [TO_DATETIME(string)] failed, treating result as null. "Only first 20 failures recorded."`

A following header will contain the failure reason and the offending value:

`"java.lang.IllegalArgumentException: failed to parse date field [1964-06-02 00:00:00] with format [yyyy-MM-dd'T'HH:mm:ss.SSS'Z']"`

If the input parameter is of a numeric type, its value will be interpreted as milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time). For example:

```esql
ROW int = [0, 1]
| EVAL dt = TO_DATETIME(int)
```

| int:integer | dt:date |
| --- | --- |
| [0, 1] | [1970-01-01T00:00:00.000Z, 1970-01-01T00:00:00.001Z] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_DATE_NANOS` [esql-to_date_nanos] 

**Syntax**

:::{image} images/to_date_nanos.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input to a nanosecond-resolution date value (aka date_nanos).

::::{note} 
The range for date nanos is 1970-01-01T00:00:00.000000000Z to 2262-04-11T23:47:16.854775807Z, attepting to convertvalues outside of that range will result in null with a warning..  Additionally, integers cannot be converted into date nanos, as the range of integer nanoseconds only covers about 2 seconds after epoch.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| date | date_nanos |
| date_nanos | date_nanos |
| double | date_nanos |
| keyword | date_nanos |
| long | date_nanos |
| text | date_nanos |
| unsigned_long | date_nanos |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_DEGREES` [esql-to_degrees] 

**Syntax**

:::{image} images/to_degrees.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a number in [radians](https://en.wikipedia.org/wiki/Radian) to [degrees](https://en.wikipedia.org/wiki/Degree_(angle)).

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW rad = [1.57, 3.14, 4.71]
| EVAL deg = TO_DEGREES(rad)
```

| rad:double | deg:double |
| --- | --- |
| [1.57, 3.14, 4.71] | [89.95437383553924, 179.9087476710785, 269.86312150661774] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_DOUBLE` [esql-to_double] 

**Syntax**

:::{image} images/to_double.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a double value. If the input parameter is of a date type, its value will be interpreted as milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), converted to double. Boolean **true** will be converted to double **1.0**, **false** to **0.0**.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | double |
| counter_double | double |
| counter_integer | double |
| counter_long | double |
| date | double |
| double | double |
| integer | double |
| keyword | double |
| long | double |
| text | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW str1 = "5.20128E11", str2 = "foo"
| EVAL dbl = TO_DOUBLE("520128000000"), dbl1 = TO_DOUBLE(str1), dbl2 = TO_DOUBLE(str2)
```

| str1:keyword | str2:keyword | dbl:double | dbl1:double | dbl2:double |
| --- | --- | --- | --- | --- |
| 5.20128E11 | foo | 5.20128E11 | 5.20128E11 | null |

Note that in this example, the last conversion of the string isn’t possible. When this happens, the result is a **null** value. In this case a *Warning* header is added to the response. The header will provide information on the source of the failure:

`"Line 1:115: evaluation of [TO_DOUBLE(str2)] failed, treating result as null. Only first 20 failures recorded."`

A following header will contain the failure reason and the offending value: `"java.lang.NumberFormatException: For input string: "foo""`

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_GEOPOINT` [esql-to_geopoint] 

**Syntax**

:::{image} images/to_geopoint.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a `geo_point` value. A string will only be successfully converted if it respects the [WKT Point](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| geo_point | geo_point |
| keyword | geo_point |
| text | geo_point |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW wkt = "POINT(42.97109630194 14.7552534413725)"
| EVAL pt = TO_GEOPOINT(wkt)
```

| wkt:keyword | pt:geo_point |
| --- | --- |
| "POINT(42.97109630194 14.7552534413725)" | POINT(42.97109630194 14.7552534413725) |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_GEOSHAPE` [esql-to_geoshape] 

**Syntax**

:::{image} images/to_geoshape.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a `geo_shape` value. A string will only be successfully converted if it respects the [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) format.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| geo_point | geo_shape |
| geo_shape | geo_shape |
| keyword | geo_shape |
| text | geo_shape |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW wkt = "POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))"
| EVAL geom = TO_GEOSHAPE(wkt)
```

| wkt:keyword | geom:geo_shape |
| --- | --- |
| "POLYGON 30 10, 40 40, 20 40, 10 20, 30 10" | POLYGON 30 10, 40 40, 20 40, 10 20, 30 10 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_INTEGER` [esql-to_integer] 

**Syntax**

:::{image} images/to_integer.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to an integer value. If the input parameter is of a date type, its value will be interpreted as milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), converted to integer. Boolean **true** will be converted to integer **1**, **false** to **0**.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | integer |
| counter_integer | integer |
| date | integer |
| double | integer |
| integer | integer |
| keyword | integer |
| long | integer |
| text | integer |
| unsigned_long | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW long = [5013792, 2147483647, 501379200000]
| EVAL int = TO_INTEGER(long)
```

| long:long | int:integer |
| --- | --- |
| [5013792, 2147483647, 501379200000] | [5013792, 2147483647] |

Note that in this example, the last value of the multi-valued field cannot be converted as an integer. When this happens, the result is a **null** value. In this case a *Warning* header is added to the response. The header will provide information on the source of the failure:

`"Line 1:61: evaluation of [TO_INTEGER(long)] failed, treating result as null. Only first 20 failures recorded."`

A following header will contain the failure reason and the offending value:

`"org.elasticsearch.xpack.esql.core.InvalidArgumentException: [501379200000] out of [integer] range"`

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_IP` [esql-to_ip] 

**Syntax**

:::{image} images/to_ip.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input string to an IP value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| ip | ip |
| keyword | ip |
| text | ip |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW str1 = "1.1.1.1", str2 = "foo"
| EVAL ip1 = TO_IP(str1), ip2 = TO_IP(str2)
| WHERE CIDR_MATCH(ip1, "1.0.0.0/8")
```

| str1:keyword | str2:keyword | ip1:ip | ip2:ip |
| --- | --- | --- | --- |
| 1.1.1.1 | foo | 1.1.1.1 | null |

Note that in this example, the last conversion of the string isn’t possible. When this happens, the result is a **null** value. In this case a *Warning* header is added to the response. The header will provide information on the source of the failure:

`"Line 1:68: evaluation of [TO_IP(str2)] failed, treating result as null. Only first 20 failures recorded."`

A following header will contain the failure reason and the offending value:

`"java.lang.IllegalArgumentException: 'foo' is not an IP string literal."`

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_LONG` [esql-to_long] 

**Syntax**

:::{image} images/to_long.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to a long value. If the input parameter is of a date type, its value will be interpreted as milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), converted to long. Boolean **true** will be converted to long **1**, **false** to **0**.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | long |
| counter_integer | long |
| counter_long | long |
| date | long |
| date_nanos | long |
| double | long |
| integer | long |
| keyword | long |
| long | long |
| text | long |
| unsigned_long | long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW str1 = "2147483648", str2 = "2147483648.2", str3 = "foo"
| EVAL long1 = TO_LONG(str1), long2 = TO_LONG(str2), long3 = TO_LONG(str3)
```

| str1:keyword | str2:keyword | str3:keyword | long1:long | long2:long | long3:long |
| --- | --- | --- | --- | --- | --- |
| 2147483648 | 2147483648.2 | foo | 2147483648 | 2147483648 | null |

Note that in this example, the last conversion of the string isn’t possible. When this happens, the result is a **null** value. In this case a *Warning* header is added to the response. The header will provide information on the source of the failure:

`"Line 1:113: evaluation of [TO_LONG(str3)] failed, treating result as null. Only first 20 failures recorded."`

A following header will contain the failure reason and the offending value:

`"java.lang.NumberFormatException: For input string: "foo""`

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_RADIANS` [esql-to_radians] 

**Syntax**

:::{image} images/to_radians.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a number in [degrees](https://en.wikipedia.org/wiki/Degree_(angle)) to [radians](https://en.wikipedia.org/wiki/Radian).

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW deg = [90.0, 180.0, 270.0]
| EVAL rad = TO_RADIANS(deg)
```

| deg:double | rad:double |
| --- | --- |
| [90.0, 180.0, 270.0] | [1.5707963267948966, 3.141592653589793, 4.71238898038469] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_STRING` [esql-to_string] 

**Syntax**

:::{image} images/to_string.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value into a string.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | keyword |
| cartesian_point | keyword |
| cartesian_shape | keyword |
| date | keyword |
| date_nanos | keyword |
| double | keyword |
| geo_point | keyword |
| geo_shape | keyword |
| integer | keyword |
| ip | keyword |
| keyword | keyword |
| long | keyword |
| text | keyword |
| unsigned_long | keyword |
| version | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW a=10
| EVAL j = TO_STRING(a)
```

| a:integer | j:keyword |
| --- | --- |
| 10 | "10" |

It also works fine on multivalued fields:

```esql
ROW a=[10, 9, 8]
| EVAL j = TO_STRING(a)
```

| a:integer | j:keyword |
| --- | --- |
| [10, 9, 8] | ["10", "9", "8"] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_TIMEDURATION` [esql-to_timeduration] 

**Syntax**

:::{image} images/to_timeduration.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input is a valid constant time duration expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value into a `time_duration` value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| keyword | time_duration |
| text | time_duration |
| time_duration | time_duration |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
row x = "2024-01-01"::datetime | eval y = x + "3 hours"::time_duration, z = x - to_timeduration("3 hours");
```

| x:datetime | y:datetime | z:datetime |
| --- | --- | --- |
| 2024-01-01 | 2024-01-01T03:00:00.000Z | 2023-12-31T21:00:00.000Z |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_UNSIGNED_LONG` [esql-to_unsigned_long] 

**Syntax**

:::{image} images/to_unsigned_long.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input value to an unsigned long value. If the input parameter is of a date type, its value will be interpreted as milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), converted to unsigned long. Boolean **true** will be converted to unsigned long **1**, **false** to **0**.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | unsigned_long |
| date | unsigned_long |
| double | unsigned_long |
| integer | unsigned_long |
| keyword | unsigned_long |
| long | unsigned_long |
| text | unsigned_long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW str1 = "2147483648", str2 = "2147483648.2", str3 = "foo"
| EVAL long1 = TO_UNSIGNED_LONG(str1), long2 = TO_ULONG(str2), long3 = TO_UL(str3)
```

| str1:keyword | str2:keyword | str3:keyword | long1:unsigned_long | long2:unsigned_long | long3:unsigned_long |
| --- | --- | --- | --- | --- | --- |
| 2147483648 | 2147483648.2 | foo | 2147483648 | 2147483648 | null |

Note that in this example, the last conversion of the string isn’t possible. When this happens, the result is a **null** value. In this case a *Warning* header is added to the response. The header will provide information on the source of the failure:

`"Line 1:133: evaluation of [TO_UL(str3)] failed, treating result as null. Only first 20 failures recorded."`

A following header will contain the failure reason and the offending value:

`"java.lang.NumberFormatException: Character f is neither a decimal digit number, decimal point, + "nor "e" notation exponential mark."`

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `TO_VERSION` [esql-to_version] 

**Syntax**

:::{image} images/to_version.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Input value. The input can be a single- or multi-valued column or an expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts an input string to a version value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| keyword | version |
| text | version |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW v = TO_VERSION("1.2.3")
```

| v:version |
| --- |
| 1.2.3 |


## {{esql}} multivalue functions [esql-mv-functions]


{{esql}} supports these multivalue functions:

%  tag::mv_list[]

* [`MV_APPEND`](esql-functions-operators.md#esql-mv_append)
* [`MV_AVG`](esql-functions-operators.md#esql-mv_avg)
* [`MV_CONCAT`](esql-functions-operators.md#esql-mv_concat)
* [`MV_COUNT`](esql-functions-operators.md#esql-mv_count)
* [`MV_DEDUPE`](esql-functions-operators.md#esql-mv_dedupe)
* [`MV_FIRST`](esql-functions-operators.md#esql-mv_first)
* [`MV_LAST`](esql-functions-operators.md#esql-mv_last)
* [`MV_MAX`](esql-functions-operators.md#esql-mv_max)
* [`MV_MEDIAN`](esql-functions-operators.md#esql-mv_median)
* [`MV_MEDIAN_ABSOLUTE_DEVIATION`](esql-functions-operators.md#esql-mv_median_absolute_deviation)
* [`MV_MIN`](esql-functions-operators.md#esql-mv_min)
* [`MV_PERCENTILE`](esql-functions-operators.md#esql-mv_percentile)
* [`MV_PSERIES_WEIGHTED_SUM`](esql-functions-operators.md#esql-mv_pseries_weighted_sum)
* [`MV_SORT`](esql-functions-operators.md#esql-mv_sort)
* [`MV_SLICE`](esql-functions-operators.md#esql-mv_slice)
* [`MV_SUM`](esql-functions-operators.md#esql-mv_sum)
* [`MV_ZIP`](esql-functions-operators.md#esql-mv_zip)

%  end::mv_list[]

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_APPEND` [esql-mv_append] 

**Syntax**

:::{image} images/mv_append.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field1`
`field2`
:   @@COMMENT@@  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


**Description**

Concatenates values of two multi-value fields.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field1 | field2 | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| cartesian_point | cartesian_point | cartesian_point |
| cartesian_shape | cartesian_shape | cartesian_shape |
| date | date | date |
| date_nanos | date_nanos | date_nanos |
| double | double | double |
| geo_point | geo_point | geo_point |
| geo_shape | geo_shape | geo_shape |
| integer | integer | integer |
| ip | ip | ip |
| keyword | keyword | keyword |
| keyword | text | keyword |
| long | long | long |
| text | keyword | keyword |
| text | text | keyword |
| unsigned_long | unsigned_long | unsigned_long |
| version | version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_AVG` [esql-mv_avg] 

**Syntax**

:::{image} images/mv_avg.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued field into a single valued field containing the average of all of the values.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | double |
| long | double |
| unsigned_long | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=[3, 5, 1, 6]
| EVAL avg_a = MV_AVG(a)
```

| a:integer | avg_a:double |
| --- | --- |
| [3, 5, 1, 6] | 3.75 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_CONCAT` [esql-mv_concat] 

**Syntax**

:::{image} images/mv_concat.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string`
:   Multivalue expression.

`delim`
:   Delimiter.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued string expression into a single valued column containing the concatenation of all values separated by a delimiter.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string | delim | result |
| --- | --- | --- |
| keyword | keyword | keyword |
| keyword | text | keyword |
| text | keyword | keyword |
| text | text | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW a=["foo", "zoo", "bar"]
| EVAL j = MV_CONCAT(a, ", ")
```

| a:keyword | j:keyword |
| --- | --- |
| ["foo", "zoo", "bar"] | "foo, zoo, bar" |

To concat non-string columns, call [`TO_STRING`](esql-functions-operators.md#esql-to_string) first:

```esql
ROW a=[10, 9, 8]
| EVAL j = MV_CONCAT(TO_STRING(a), ", ")
```

| a:integer | j:keyword |
| --- | --- |
| [10, 9, 8] | "10, 9, 8" |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_COUNT` [esql-mv_count] 

**Syntax**

:::{image} images/mv_count.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued expression into a single valued column containing a count of the number of values.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | integer |
| cartesian_point | integer |
| cartesian_shape | integer |
| date | integer |
| date_nanos | integer |
| double | integer |
| geo_point | integer |
| geo_shape | integer |
| integer | integer |
| ip | integer |
| keyword | integer |
| long | integer |
| text | integer |
| unsigned_long | integer |
| version | integer |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=["foo", "zoo", "bar"]
| EVAL count_a = MV_COUNT(a)
```

| a:keyword | count_a:integer |
| --- | --- |
| ["foo", "zoo", "bar"] | 3 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_DEDUPE` [esql-mv_dedupe] 

**Syntax**

:::{image} images/mv_dedupe.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Remove duplicate values from a multivalued field.

::::{note} 
`MV_DEDUPE` may, but won’t always, sort the values in the column.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| cartesian_point | cartesian_point |
| cartesian_shape | cartesian_shape |
| date | date |
| date_nanos | date_nanos |
| double | double |
| geo_point | geo_point |
| geo_shape | geo_shape |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| unsigned_long | unsigned_long |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=["foo", "foo", "bar", "foo"]
| EVAL dedupe_a = MV_DEDUPE(a)
```

| a:keyword | dedupe_a:keyword |
| --- | --- |
| ["foo", "foo", "bar", "foo"] | ["foo", "bar"] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_FIRST` [esql-mv_first] 

**Syntax**

:::{image} images/mv_first.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued expression into a single valued column containing the first value. This is most useful when reading from a function that emits multivalued columns in a known order like [`SPLIT`](esql-functions-operators.md#esql-split).

The order that [multivalued fields](esql-multivalued-fields.md) are read from underlying storage is not guaranteed. It is **frequently** ascending, but don’t rely on that. If you need the minimum value use [`MV_MIN`](esql-functions-operators.md#esql-mv_min) instead of `MV_FIRST`. `MV_MIN` has optimizations for sorted values so there isn’t a performance benefit to `MV_FIRST`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| cartesian_point | cartesian_point |
| cartesian_shape | cartesian_shape |
| date | date |
| date_nanos | date_nanos |
| double | double |
| geo_point | geo_point |
| geo_shape | geo_shape |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| unsigned_long | unsigned_long |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a="foo;bar;baz"
| EVAL first_a = MV_FIRST(SPLIT(a, ";"))
```

| a:keyword | first_a:keyword |
| --- | --- |
| foo;bar;baz | "foo" |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_LAST` [esql-mv_last] 

**Syntax**

:::{image} images/mv_last.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalue expression into a single valued column containing the last value. This is most useful when reading from a function that emits multivalued columns in a known order like [`SPLIT`](esql-functions-operators.md#esql-split).

The order that [multivalued fields](esql-multivalued-fields.md) are read from underlying storage is not guaranteed. It is **frequently** ascending, but don’t rely on that. If you need the maximum value use [`MV_MAX`](esql-functions-operators.md#esql-mv_max) instead of `MV_LAST`. `MV_MAX` has optimizations for sorted values so there isn’t a performance benefit to `MV_LAST`.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| cartesian_point | cartesian_point |
| cartesian_shape | cartesian_shape |
| date | date |
| date_nanos | date_nanos |
| double | double |
| geo_point | geo_point |
| geo_shape | geo_shape |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| unsigned_long | unsigned_long |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a="foo;bar;baz"
| EVAL last_a = MV_LAST(SPLIT(a, ";"))
```

| a:keyword | last_a:keyword |
| --- | --- |
| foo;bar;baz | "baz" |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_MAX` [esql-mv_max] 

**Syntax**

:::{image} images/mv_max.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued expression into a single valued column containing the maximum value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| date | date |
| date_nanos | date_nanos |
| double | double |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| unsigned_long | unsigned_long |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW a=[3, 5, 1]
| EVAL max_a = MV_MAX(a)
```

| a:integer | max_a:integer |
| --- | --- |
| [3, 5, 1] | 5 |

It can be used by any column type, including `keyword` columns. In that case it picks the last string, comparing their utf-8 representation byte by byte:

```esql
ROW a=["foo", "zoo", "bar"]
| EVAL max_a = MV_MAX(a)
```

| a:keyword | max_a:keyword |
| --- | --- |
| ["foo", "zoo", "bar"] | "zoo" |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_MEDIAN` [esql-mv_median] 

**Syntax**

:::{image} images/mv_median.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued field into a single valued field containing the median value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | integer |
| long | long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW a=[3, 5, 1]
| EVAL median_a = MV_MEDIAN(a)
```

| a:integer | median_a:integer |
| --- | --- |
| [3, 5, 1] | 3 |

If the row has an even number of values for a column, the result will be the average of the middle two entries. If the column is not floating point, the average rounds **down**:

```esql
ROW a=[3, 7, 1, 6]
| EVAL median_a = MV_MEDIAN(a)
```

| a:integer | median_a:integer |
| --- | --- |
| [3, 7, 1, 6] | 4 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_MEDIAN_ABSOLUTE_DEVIATION` [esql-mv_median_absolute_deviation] 

**Syntax**

:::{image} images/mv_median_absolute_deviation.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued field into a single valued field containing the median absolute deviation.  It is calculated as the median of each data point’s deviation from the median of the entire sample. That is, for a random variable `X`, the median absolute deviation is `median(|median(X) - X|)`.

::::{note} 
If the field has an even number of values, the medians will be calculated as the average of the middle two values. If the value is not a floating point number, the averages are rounded towards 0.
::::


%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | integer |
| long | long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW values = [0, 2, 5, 6]
| EVAL median_absolute_deviation = MV_MEDIAN_ABSOLUTE_DEVIATION(values), median = MV_MEDIAN(values)
```

| values:integer | median_absolute_deviation:integer | median:integer |
| --- | --- | --- |
| [0, 2, 5, 6] | 2 | 3 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_MIN` [esql-mv_min] 

**Syntax**

:::{image} images/mv_min.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued expression into a single valued column containing the minimum value.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| boolean | boolean |
| date | date |
| date_nanos | date_nanos |
| double | double |
| integer | integer |
| ip | ip |
| keyword | keyword |
| long | long |
| text | keyword |
| unsigned_long | unsigned_long |
| version | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
ROW a=[2, 1]
| EVAL min_a = MV_MIN(a)
```

| a:integer | min_a:integer |
| --- | --- |
| [2, 1] | 1 |

It can be used by any column type, including `keyword` columns. In that case, it picks the first string, comparing their utf-8 representation byte by byte:

```esql
ROW a=["foo", "bar"]
| EVAL min_a = MV_MIN(a)
```

| a:keyword | min_a:keyword |
| --- | --- |
| ["foo", "bar"] | "bar" |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_PERCENTILE` [esql-mv_percentile] 

**Syntax**

:::{image} images/mv_percentile.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Multivalue expression.

`percentile`
:   The percentile to calculate. Must be a number between 0 and 100. Numbers out of range will return a null instead.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued field into a single valued field containing the value at which a certain percentage of observed values occur.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | percentile | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | integer |
| integer | integer | integer |
| integer | long | integer |
| long | double | long |
| long | integer | long |
| long | long | long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW values = [5, 5, 10, 12, 5000]
| EVAL p50 = MV_PERCENTILE(values, 50), median = MV_MEDIAN(values)
```

| values:integer | p50:integer | median:integer |
| --- | --- | --- |
| [5, 5, 10, 12, 5000] | 10 | 10 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_PSERIES_WEIGHTED_SUM` [esql-mv_pseries_weighted_sum] 

**Syntax**

:::{image} images/mv_pseries_weighted_sum.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Multivalue expression.

`p`
:   It is a constant number that represents the *p* parameter in the P-Series. It impacts every element’s contribution to the weighted sum.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued expression into a single-valued column by multiplying every element on the input list by its corresponding term in P-Series and computing the sum.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | p | result |
| --- | --- | --- |
| double | double | double |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = [70.0, 45.0, 21.0, 21.0, 21.0]
| EVAL sum = MV_PSERIES_WEIGHTED_SUM(a, 1.5)
| KEEP sum
```

| sum:double |
| --- |
| 94.45465156212452 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_SLICE` [esql-mv_slice] 

**Syntax**

:::{image} images/mv_slice.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression. If `null`, the function returns `null`.

`start`
:   Start position. If `null`, the function returns `null`. The start argument can be negative. An index of -1 is used to specify the last value in the list.

`end`
:   End position(included). Optional; if omitted, the position at `start` is returned. The end argument can be negative. An index of -1 is used to specify the last value in the list.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Returns a subset of the multivalued field using the start and end index values. This is most useful when reading from a function that emits multivalued columns in a known order like [`SPLIT`](esql-functions-operators.md#esql-split) or [`MV_SORT`](esql-functions-operators.md#esql-mv_sort).

The order that [multivalued fields](esql-multivalued-fields.md) are read from underlying storage is not guaranteed. It is **frequently** ascending, but don’t rely on that.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | start | end | result |
| --- | --- | --- | --- |
| boolean | integer | integer | boolean |
| cartesian_point | integer | integer | cartesian_point |
| cartesian_shape | integer | integer | cartesian_shape |
| date | integer | integer | date |
| date_nanos | integer | integer | date_nanos |
| double | integer | integer | double |
| geo_point | integer | integer | geo_point |
| geo_shape | integer | integer | geo_shape |
| integer | integer | integer | integer |
| ip | integer | integer | ip |
| keyword | integer | integer | keyword |
| long | integer | integer | long |
| text | integer | integer | keyword |
| unsigned_long | integer | integer | unsigned_long |
| version | integer | integer | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Examples**

```esql
row a = [1, 2, 2, 3]
| eval a1 = mv_slice(a, 1), a2 = mv_slice(a, 2, 3)
```

| a:integer | a1:integer | a2:integer |
| --- | --- | --- |
| [1, 2, 2, 3] | 2 | [2, 3] |

```esql
row a = [1, 2, 2, 3]
| eval a1 = mv_slice(a, -2), a2 = mv_slice(a, -3, -1)
```

| a:integer | a1:integer | a2:integer |
| --- | --- | --- |
| [1, 2, 2, 3] | 2 | [2, 2, 3] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_SORT` [esql-mv_sort] 

**Syntax**

:::{image} images/mv_sort.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`field`
:   Multivalue expression. If `null`, the function returns `null`.

`order`
:   Sort order. The valid options are ASC and DESC, the default is ASC.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Sorts a multivalued field in lexicographical order.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | order | result |
| --- | --- | --- |
| boolean | keyword | boolean |
| date | keyword | date |
| date_nanos | keyword | date_nanos |
| double | keyword | double |
| integer | keyword | integer |
| ip | keyword | ip |
| keyword | keyword | keyword |
| long | keyword | long |
| text | keyword | keyword |
| version | keyword | version |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = [4, 2, -3, 2]
| EVAL sa = mv_sort(a), sd = mv_sort(a, "DESC")
```

| a:integer | sa:integer | sd:integer |
| --- | --- | --- |
| [4, 2, -3, 2] | [-3, 2, 2, 4] | [4, 2, 2, -3] |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_SUM` [esql-mv_sum] 

**Syntax**

:::{image} images/mv_sum.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`number`
:   Multivalue expression.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Converts a multivalued field into a single valued field containing the sum of all of the values.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| number | result |
| --- | --- |
| double | double |
| integer | integer |
| long | long |
| unsigned_long | unsigned_long |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a=[3, 5, 6]
| EVAL sum_a = MV_SUM(a)
```

| a:integer | sum_a:integer |
| --- | --- |
| [3, 5, 6] | 14 |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.


## `MV_ZIP` [esql-mv_zip] 

**Syntax**

:::{image} images/mv_zip.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Parameters**

`string1`
:   Multivalue expression.

`string2`
:   Multivalue expression.

`delim`
:   Delimiter. Optional; if omitted, `,` is used as a default delimiter.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Description**

Combines the values from two multivalued fields with a delimiter that joins them together.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| string1 | string2 | delim | result |
| --- | --- | --- | --- |
| keyword | keyword | keyword | keyword |
| keyword | keyword | text | keyword |
| keyword | keyword |  | keyword |
| keyword | text | keyword | keyword |
| keyword | text | text | keyword |
| keyword | text |  | keyword |
| text | keyword | keyword | keyword |
| text | keyword | text | keyword |
| text | keyword |  | keyword |
| text | text | keyword | keyword |
| text | text | text | keyword |
| text | text |  | keyword |

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Example**

```esql
ROW a = ["x", "y", "z"], b = ["1", "2"]
| EVAL c = mv_zip(a, b, "-")
| KEEP a, b, c
```

| a:keyword | b:keyword | c:keyword |
| --- | --- | --- |
| [x, y, z] | [1 ,2] | [x-1, y-2, z] |


## {{esql}} operators [esql-operators]


Boolean operators for comparing against one or multiple expressions.

%  tag::op_list[]

* [Binary operators](esql-functions-operators.md#esql-binary-operators)
* [Unary operators](esql-functions-operators.md#esql-unary-operators)
* [Logical operators](esql-functions-operators.md#esql-logical-operators)
* [`IS NULL` and `IS NOT NULL` predicates](esql-functions-operators.md#esql-predicates)
* [`Cast (::)`](esql-functions-operators.md#esql-cast-operator)
* [`IN`](esql-functions-operators.md#esql-in-operator)
* [`LIKE`](esql-functions-operators.md#esql-like-operator)
* [`RLIKE`](esql-functions-operators.md#esql-rlike-operator)
* [preview] [Search operators](esql-functions-operators.md#esql-search-operators)

%  end::op_list[]


## Binary operators [esql-binary-operators] 


## Equality [esql-binary-operators-equality]

:::{image} images/equals.svg
:alt: Embedded
:class: text-center
:::

Check if two fields are equal. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
This is pushed to the underlying search index if one side of the comparison is constant and the other side is a field in the index that has both an [`index`](mapping-index.md) and [`doc_values`](doc-values.md).
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| cartesian_point | cartesian_point | boolean |
| cartesian_shape | cartesian_shape | boolean |
| date | date | boolean |
| date | date_nanos | boolean |
| date_nanos | date | boolean |
| date_nanos | date_nanos | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | long | boolean |
| geo_point | geo_point | boolean |
| geo_shape | geo_shape | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| keyword | keyword | boolean |
| keyword | text | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | long | boolean |
| text | keyword | boolean |
| text | text | boolean |
| unsigned_long | unsigned_long | boolean |
| version | version | boolean |


## Inequality `!=` [_inequality]

:::{image} images/not_equals.svg
:alt: Embedded
:class: text-center
:::

Check if two fields are unequal. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
This is pushed to the underlying search index if one side of the comparison is constant and the other side is a field in the index that has both an [`index`](mapping-index.md) and [`doc_values`](doc-values.md).
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| cartesian_point | cartesian_point | boolean |
| cartesian_shape | cartesian_shape | boolean |
| date | date | boolean |
| date | date_nanos | boolean |
| date_nanos | date | boolean |
| date_nanos | date_nanos | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | long | boolean |
| geo_point | geo_point | boolean |
| geo_shape | geo_shape | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| keyword | keyword | boolean |
| keyword | text | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | long | boolean |
| text | keyword | boolean |
| text | text | boolean |
| unsigned_long | unsigned_long | boolean |
| version | version | boolean |


## Less than `<` [_less_than]

:::{image} images/less_than.svg
:alt: Embedded
:class: text-center
:::

Check if one field is less than another. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
This is pushed to the underlying search index if one side of the comparison is constant and the other side is a field in the index that has both an [`index`](mapping-index.md) and [`doc_values`](doc-values.md).
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| date | date | boolean |
| date | date_nanos | boolean |
| date_nanos | date | boolean |
| date_nanos | date_nanos | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | long | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| keyword | keyword | boolean |
| keyword | text | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | long | boolean |
| text | keyword | boolean |
| text | text | boolean |
| unsigned_long | unsigned_long | boolean |
| version | version | boolean |


## Less than or equal to `<=` [_less_than_or_equal_to]

:::{image} images/less_than_or_equal.svg
:alt: Embedded
:class: text-center
:::

Check if one field is less than or equal to another. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
This is pushed to the underlying search index if one side of the comparison is constant and the other side is a field in the index that has both an [`index`](mapping-index.md) and [`doc_values`](doc-values.md).
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| date | date | boolean |
| date | date_nanos | boolean |
| date_nanos | date | boolean |
| date_nanos | date_nanos | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | long | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| keyword | keyword | boolean |
| keyword | text | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | long | boolean |
| text | keyword | boolean |
| text | text | boolean |
| unsigned_long | unsigned_long | boolean |
| version | version | boolean |


## Greater than `>` [_greater_than]

:::{image} images/greater_than.svg
:alt: Embedded
:class: text-center
:::

Check if one field is greater than another. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
This is pushed to the underlying search index if one side of the comparison is constant and the other side is a field in the index that has both an [`index`](mapping-index.md) and [`doc_values`](doc-values.md).
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| date | date | boolean |
| date | date_nanos | boolean |
| date_nanos | date | boolean |
| date_nanos | date_nanos | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | long | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| keyword | keyword | boolean |
| keyword | text | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | long | boolean |
| text | keyword | boolean |
| text | text | boolean |
| unsigned_long | unsigned_long | boolean |
| version | version | boolean |


## Greater than or equal to `>=` [_greater_than_or_equal_to]

:::{image} images/greater_than_or_equal.svg
:alt: Embedded
:class: text-center
:::

Check if one field is greater than or equal to another. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
This is pushed to the underlying search index if one side of the comparison is constant and the other side is a field in the index that has both an [`index`](mapping-index.md) and [`doc_values`](doc-values.md).
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| date | date | boolean |
| date | date_nanos | boolean |
| date_nanos | date | boolean |
| date_nanos | date_nanos | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | long | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| keyword | keyword | boolean |
| keyword | text | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | long | boolean |
| text | keyword | boolean |
| text | text | boolean |
| unsigned_long | unsigned_long | boolean |
| version | version | boolean |


## Add `+` [esql-add]

:::{image} images/add.svg
:alt: Embedded
:class: text-center
:::

Add two numbers together. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| date | date_period | date |
| date | time_duration | date |
| date_nanos | date_period | date_nanos |
| date_nanos | time_duration | date_nanos |
| date_period | date | date |
| date_period | date_nanos | date_nanos |
| date_period | date_period | date_period |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | integer |
| integer | long | long |
| long | double | double |
| long | integer | long |
| long | long | long |
| time_duration | date | date |
| time_duration | date_nanos | date_nanos |
| time_duration | time_duration | time_duration |
| unsigned_long | unsigned_long | unsigned_long |


## Subtract `-` [esql-subtract]

:::{image} images/sub.svg
:alt: Embedded
:class: text-center
:::

Subtract one number from another. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| date | date_period | date |
| date | time_duration | date |
| date_nanos | date_period | date_nanos |
| date_nanos | time_duration | date_nanos |
| date_period | date_nanos | date_nanos |
| date_period | date_period | date_period |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | integer |
| integer | long | long |
| long | double | double |
| long | integer | long |
| long | long | long |
| time_duration | date_nanos | date_nanos |
| time_duration | time_duration | time_duration |
| unsigned_long | unsigned_long | unsigned_long |


## Multiply `*` [_multiply]

:::{image} images/mul.svg
:alt: Embedded
:class: text-center
:::

Multiply two numbers together. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | integer |
| integer | long | long |
| long | double | double |
| long | integer | long |
| long | long | long |
| unsigned_long | unsigned_long | unsigned_long |


## Divide `/` [_divide]

:::{image} images/div.svg
:alt: Embedded
:class: text-center
:::

Divide one number by another. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

::::{note} 
Division of two integer types will yield an integer result, rounding towards 0. If you need floating point division, [`Cast (::)`](esql-functions-operators.md#esql-cast-operator) one of the arguments to a `DOUBLE`.
::::


Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | integer |
| integer | long | long |
| long | double | double |
| long | integer | long |
| long | long | long |
| unsigned_long | unsigned_long | unsigned_long |


## Modulus `%` [_modulus]

:::{image} images/mod.svg
:alt: Embedded
:class: text-center
:::

Divide one number by another and return the remainder. If either field is [multivalued](esql-multivalued-fields.md) then the result is `null`.

Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| lhs | rhs | result |
| --- | --- | --- |
| double | double | double |
| double | integer | double |
| double | long | double |
| integer | double | double |
| integer | integer | integer |
| integer | long | long |
| long | double | double |
| long | integer | long |
| long | long | long |
| unsigned_long | unsigned_long | unsigned_long |


## Unary operators [esql-unary-operators] 

The only unary operators is negation (`-`):

:::{image} images/neg.svg
:alt: Embedded
:class: text-center
:::

Supported types:

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | result |
| --- | --- |
| date_period | date_period |
| double | double |
| integer | integer |
| long | long |
| time_duration | time_duration |


## Logical operators [esql-logical-operators] 

The following logical operators are supported:

* `AND`
* `OR`
* `NOT`


## `IS NULL` and `IS NOT NULL` predicates [esql-predicates] 

% tag::body[]

For NULL comparison, use the `IS NULL` and `IS NOT NULL` predicates:

```esql
FROM employees
| WHERE birth_date IS NULL
| KEEP first_name, last_name
| SORT first_name
| LIMIT 3
```

| first_name:keyword | last_name:keyword |
| --- | --- |
| Basil | Tramer |
| Florian | Syrotiuk |
| Lucien | Rosenbaum |

```esql
FROM employees
| WHERE is_rehired IS NOT NULL
| STATS COUNT(emp_no)
```

| COUNT(emp_no):long |
| --- |
| 84 |

% end::body[]


## `Cast (::)` [esql-cast-operator]

%  tag::body[]

The `::` operator provides a convenient alternative syntax to the TO_<type> [conversion functions](esql-functions-operators.md#esql-type-conversion-functions).

```esql
ROW ver = CONCAT(("0"::INT + 1)::STRING, ".2.3")::VERSION
```

| ver:version |
| --- |
| 1.2.3 |

%  end::body[]


## `IN` [esql-in-operator] 

% tag::body[]

The `IN` operator allows testing whether a field or expression equals an element in a list of literals, fields or expressions:

```esql
ROW a = 1, b = 4, c = 3
| WHERE c-a IN (3, b / 2, a)
```

| a:integer | b:integer | c:integer |
| --- | --- | --- |
| 1 | 4 | 3 |

% end::body[]


## `LIKE` [esql-like-operator] 

%  tag::body[]

Use `LIKE` to filter data based on string patterns using wildcards. `LIKE` usually acts on a field placed on the left-hand side of the operator, but it can also act on a constant (literal) expression. The right-hand side of the operator represents the pattern.

The following wildcard characters are supported:

* `*` matches zero or more characters.
* `?` matches one character.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | pattern | result |
| --- | --- | --- |
| keyword | keyword | boolean |
| text | keyword | boolean |

```esql
FROM employees
| WHERE first_name LIKE """?b*"""
| KEEP first_name, last_name
```

| first_name:keyword | last_name:keyword |
| --- | --- |
| Ebbe | Callaway |
| Eberhardt | Terkki |

Matching the exact characters `*` and `.` will require escaping. The escape character is backslash `\`. Since also backslash is a special character in string literals, it will require further escaping.

```esql
ROW message = "foo * bar"
| WHERE message LIKE "foo \\* bar"
```

To reduce the overhead of escaping, we suggest using triple quotes strings `"""`

```esql
ROW message = "foo * bar"
| WHERE message LIKE """foo \* bar"""
```

%  end::body[]


## `RLIKE` [esql-rlike-operator]

%  tag::body[]

Use `RLIKE` to filter data based on string patterns using using [regular expressions](regexp-syntax.md). `RLIKE` usually acts on a field placed on the left-hand side of the operator, but it can also act on a constant (literal) expression. The right-hand side of the operator represents the pattern.

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| str | pattern | result |
| --- | --- | --- |
| keyword | keyword | boolean |
| text | keyword | boolean |

```esql
FROM employees
| WHERE first_name RLIKE """.leja.*"""
| KEEP first_name, last_name
```

| first_name:keyword | last_name:keyword |
| --- | --- |
| Alejandro | McAlpine |

Matching special characters (eg. `.`, `*`, `(`…​) will require escaping. The escape character is backslash `\`. Since also backslash is a special character in string literals, it will require further escaping.

```esql
ROW message = "foo ( bar"
| WHERE message RLIKE "foo \\( bar"
```

To reduce the overhead of escaping, we suggest using triple quotes strings `"""`

```esql
ROW message = "foo ( bar"
| WHERE message RLIKE """foo \( bar"""
```

%  end::body[]


## Search operators [esql-search-operators] 

The only search operator is match (`:`).

::::{warning} 
Do not use on production environments. This functionality is in technical preview and may be changed or removed in a future release. Elastic will work to fix any issues, but features in technical preview are not subject to the support SLA of official GA features.
::::


The match operator performs a [match query](query-dsl-match-query.md) on the specified field. Returns true if the provided query matches the row.

The match operator is equivalent to the [match function](esql-functions-operators.md#esql-match).

For using the function syntax, or adding [match query parameters](query-dsl-match-query.md#match-field-params), you can use the [match function](esql-functions-operators.md#esql-match).

:::{image} images/match_operator.svg
:alt: Embedded
:class: text-center
:::

%  This is generated by ESQL’s AbstractFunctionTestCase. Do no edit it. See ../README.md for how to regenerate it.

**Supported types**

| field | query | result |
| --- | --- | --- |
| boolean | boolean | boolean |
| boolean | keyword | boolean |
| date | date | boolean |
| date | keyword | boolean |
| date_nanos | date_nanos | boolean |
| date_nanos | keyword | boolean |
| double | double | boolean |
| double | integer | boolean |
| double | keyword | boolean |
| double | long | boolean |
| integer | double | boolean |
| integer | integer | boolean |
| integer | keyword | boolean |
| integer | long | boolean |
| ip | ip | boolean |
| ip | keyword | boolean |
| keyword | keyword | boolean |
| long | double | boolean |
| long | integer | boolean |
| long | keyword | boolean |
| long | long | boolean |
| text | keyword | boolean |
| unsigned_long | double | boolean |
| unsigned_long | integer | boolean |
| unsigned_long | keyword | boolean |
| unsigned_long | long | boolean |
| unsigned_long | unsigned_long | boolean |
| version | keyword | boolean |
| version | version | boolean |

```esql
FROM books
| WHERE author:"Faulkner"
| KEEP book_no, author
| SORT book_no
| LIMIT 5
```

| book_no:keyword | author:text |
| --- | --- |
| 2378 | [Carol Faulkner, Holly Byers Ochoa, Lucretia Mott] |
| 2713 | William Faulkner |
| 2847 | Colleen Faulkner |
| 2883 | William Faulkner |
| 3293 | Danny Faulkner |


