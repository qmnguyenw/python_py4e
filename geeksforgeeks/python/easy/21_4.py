Python | Pandas DataFrame.fillna() to replace Null values in dataframe



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages, and makes importing and analyzing data much easier.

Sometimes csv file has null values, which are later displayed as _NaN_ in Data
Frame. Just like pandas dropna() method manage and remove Null values from a
data frame, fillna() manages and let the user replace NaN values with some
value of their own.  

 **Syntax:**

> DataFrame.fillna(value=None, method=None, axis=None, inplace=False,
> limit=None, downcast=None, **kwargs)

 **Parameters:**

  

  

>  **value :** Static, dictionary, array, series or dataframe to fill instead
> of NaN.  
>  **method :** Method is used if user doesn’t pass any value. Pandas has
> different methods like bfill, backfill or ffill which fills the place
> with value in the Forward index or Previous/Back respectively.

