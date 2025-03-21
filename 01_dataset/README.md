<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h1 id="Dataset-Information-and-Exploration"><div align="center">Dataset Information and Exploration</div><a class="anchor-link" href="#Dataset-Information-and-Exploration"></a></h1>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="About-Dataset">About Dataset<a class="anchor-link" href="#About-Dataset"></a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Sales-Data-Description">Sales Data Description<a class="anchor-link" href="#Sales-Data-Description"></a></h3><p>This dataset represents synthetic sales data generated for practice purposes only. It is not real-time or based on actual business operations, and should be used solely for educational or testing purposes. The dataset contains information that simulates sales transactions across different products, regions, and customers. Each row represents an individual sale event with various details associated with it.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Columns-in-the-Dataset">Columns in the Dataset<a class="anchor-link" href="#Columns-in-the-Dataset"></a></h3><ul>
<li><p><b>Product_ID</b>: Unique identifier for each product sold. Randomly generated for practice purposes.</p>
</li>
<li><p><b>Sale_Date</b>: The date when the sale occurred. Randomly selected from the year 2023.</p>
</li>
<li><p><b>Sales_Rep</b>: The sales representative responsible for the transaction. The dataset includes five random sales representatives (Alice, Bob, Charlie, David, Eve).</p>
</li>
<li><p><b>Region</b>: The region where the sale took place. The possible regions are North, South, East, and West.</p>
</li>
<li><p><b>Sales_Amount</b>: The total sales amount for the transaction, including discounts if any. Values range from 100 to 10,000 (in currency units).</p>
</li>
<li><p><b>Quantity_Sold</b>: The number of units sold in that transaction, randomly generated between 1 and 50.</p>
</li>
<li><p><b>Product_Category</b>: The category of the product sold. Categories include Electronics, Furniture, Clothing, and Food.</p>
</li>
<li><p><b>Unit_Cost</b>: The cost per unit of the product sold, randomly generated between 50 and 5000 currency units.</p>
</li>
<li><p><b>Unit_Price</b>: The selling price per unit of the product, calculated to be higher than the unit cost.</p>
</li>
<li><p><b>Customer_Type</b>: Indicates whether the customer is a New or Returning customer.</p>
</li>
<li><p><b>Discount</b>: The discount applied to the sale, randomly chosen between 0% and 30%.</p>
</li>
<li><p><b>Payment_Method</b>: The method of payment used by the customer (e.g., Credit Card, Cash, Bank Transfer).</p>
</li>
<li><p><b>Sales_Channel</b>: The channel through which the sale occurred. Either Online or Retail.</p>
</li>
<li><p><b>Region_and_Sales_Rep</b>: A combined column that pairs the region and sales representative for easier tracking.</p>
</li>
</ul>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Disclaimer">Disclaimer<a class="anchor-link" href="#Disclaimer"></a></h3><p>This data was randomly generated and is intended solely for practice, learning, or testing. It does not reflect real-world sales, customers, or businesses, and should not be considered reliable for any real-time analysis or decision-making.</p>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Dataset-Exploration">Dataset Exploration<a class="anchor-link" href="#Dataset-Exploration"></a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Import-necessary-libraries:">Import necessary libraries:<a class="anchor-link" href="#Import-necessary-libraries:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">os</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">zipfile</span><span class="w"> </span><span class="kn">import</span> <span class="n">ZipFile</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">pandas</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Download-and-unzip-data-file:">Download and unzip data file:<a class="anchor-link" href="#Download-and-unzip-data-file:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">zip_dir</span> <span class="o">=</span> <span class="s2">"/home/intergalacticmule/repos/sales-data-analysis/dataset/"</span>
<span class="n">zip_name</span> <span class="o">=</span> <span class="s2">"sales_data.zip"</span>
<span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="sa">f</span><span class="s2">"curl -L -o </span><span class="si">{</span><span class="n">zip_dir</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">zip_name</span><span class="si">}</span><span class="s2"> https://www.kaggle.com/api/v1/datasets/download/vinothkannaece/sales-dataset/"</span><span class="p">)</span>

<span class="k">with</span> <span class="n">ZipFile</span><span class="p">(</span><span class="n">zip_dir</span> <span class="o">+</span> <span class="n">zip_name</span><span class="p">,</span> <span class="s1">'r'</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_file</span><span class="p">:</span>
    <span class="n">zip_file</span><span class="o">.</span><span class="n">extractall</span><span class="p">(</span><span class="n">zip_dir</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
<pre>  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 27634  100 27634    0     0  41161      0 --:--:-- --:--:-- --:--:-- 41161
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Load-the-dataset:">Load the dataset:<a class="anchor-link" href="#Load-the-dataset:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pandas</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="n">zip_dir</span> <span class="o">+</span> <span class="n">zip_name</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s2">"zip"</span><span class="p">,</span> <span class="s2">"csv"</span><span class="p">))</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Display-dataframe-head:">Display dataframe head:<a class="anchor-link" href="#Display-dataframe-head:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>Product_ID</th>
<th>Sale_Date</th>
<th>Sales_Rep</th>
<th>Region</th>
<th>Sales_Amount</th>
<th>Quantity_Sold</th>
<th>Product_Category</th>
<th>Unit_Cost</th>
<th>Unit_Price</th>
<th>Customer_Type</th>
<th>Discount</th>
<th>Payment_Method</th>
<th>Sales_Channel</th>
<th>Region_and_Sales_Rep</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>1052</td>
<td>2023-02-03</td>
<td>Bob</td>
<td>North</td>
<td>5053.97</td>
<td>18</td>
<td>Furniture</td>
<td>152.75</td>
<td>267.22</td>
<td>Returning</td>
<td>0.09</td>
<td>Cash</td>
<td>Online</td>
<td>North-Bob</td>
</tr>
<tr>
<th>1</th>
<td>1093</td>
<td>2023-04-21</td>
<td>Bob</td>
<td>West</td>
<td>4384.02</td>
<td>17</td>
<td>Furniture</td>
<td>3816.39</td>
<td>4209.44</td>
<td>Returning</td>
<td>0.11</td>
<td>Cash</td>
<td>Retail</td>
<td>West-Bob</td>
</tr>
<tr>
<th>2</th>
<td>1015</td>
<td>2023-09-21</td>
<td>David</td>
<td>South</td>
<td>4631.23</td>
<td>30</td>
<td>Food</td>
<td>261.56</td>
<td>371.40</td>
<td>Returning</td>
<td>0.20</td>
<td>Bank Transfer</td>
<td>Retail</td>
<td>South-David</td>
</tr>
<tr>
<th>3</th>
<td>1072</td>
<td>2023-08-24</td>
<td>Bob</td>
<td>South</td>
<td>2167.94</td>
<td>39</td>
<td>Clothing</td>
<td>4330.03</td>
<td>4467.75</td>
<td>New</td>
<td>0.02</td>
<td>Credit Card</td>
<td>Retail</td>
<td>South-Bob</td>
</tr>
<tr>
<th>4</th>
<td>1061</td>
<td>2023-03-24</td>
<td>Charlie</td>
<td>East</td>
<td>3750.20</td>
<td>13</td>
<td>Electronics</td>
<td>637.37</td>
<td>692.71</td>
<td>New</td>
<td>0.08</td>
<td>Credit Card</td>
<td>Online</td>
<td>East-Charlie</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Display-dataframe-info:">Display dataframe info:<a class="anchor-link" href="#Display-dataframe-info:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
<pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
RangeIndex: 1000 entries, 0 to 999
Data columns (total 14 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Product_ID            1000 non-null   int64  
 1   Sale_Date             1000 non-null   object 
 2   Sales_Rep             1000 non-null   object 
 3   Region                1000 non-null   object 
 4   Sales_Amount          1000 non-null   float64
 5   Quantity_Sold         1000 non-null   int64  
 6   Product_Category      1000 non-null   object 
 7   Unit_Cost             1000 non-null   float64
 8   Unit_Price            1000 non-null   float64
 9   Customer_Type         1000 non-null   object 
 10  Discount              1000 non-null   float64
 11  Payment_Method        1000 non-null   object 
 12  Sales_Channel         1000 non-null   object 
 13  Region_and_Sales_Rep  1000 non-null   object 
dtypes: float64(4), int64(2), object(8)
memory usage: 109.5+ KB
</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Check-for-duplicates">Check for duplicates<a class="anchor-link" href="#Check-for-duplicates"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Product_ID              1000
Sale_Date               1000
Sales_Rep               1000
Region                  1000
Sales_Amount            1000
Quantity_Sold           1000
Product_Category        1000
Unit_Cost               1000
Unit_Price              1000
Customer_Type           1000
Discount                1000
Payment_Method          1000
Sales_Channel           1000
Region_and_Sales_Rep    1000
dtype: int64</pre>
</div>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df2</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">drop_duplicates</span><span class="p">()</span>
<span class="n">df2</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
<pre>Product_ID              1000
Sale_Date               1000
Sales_Rep               1000
Region                  1000
Sales_Amount            1000
Quantity_Sold           1000
Product_Category        1000
Unit_Cost               1000
Unit_Price              1000
Customer_Type           1000
Discount                1000
Payment_Method          1000
Sales_Channel           1000
Region_and_Sales_Rep    1000
dtype: int64</pre>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Convert-Sale_Date-to-datetime:">Convert Sale_Date to datetime:<a class="anchor-link" href="#Convert-Sale_Date-to-datetime:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="p">[</span><span class="s1">'Sale_Date'</span><span class="p">]</span> <span class="o">=</span> <span class="n">pandas</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'Sale_Date'</span><span class="p">])</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="View-descriptive-statistics:">View descriptive statistics:<a class="anchor-link" href="#View-descriptive-statistics:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>Product_ID</th>
<th>Sale_Date</th>
<th>Sales_Amount</th>
<th>Quantity_Sold</th>
<th>Unit_Cost</th>
<th>Unit_Price</th>
<th>Discount</th>
</tr>
</thead>
<tbody>
<tr>
<th>count</th>
<td>1000.000000</td>
<td>1000</td>
<td>1000.000000</td>
<td>1000.000000</td>
<td>1000.000000</td>
<td>1000.000000</td>
<td>1000.00000</td>
</tr>
<tr>
<th>mean</th>
<td>1050.128000</td>
<td>2023-07-02 17:42:43.199999744</td>
<td>5019.265230</td>
<td>25.355000</td>
<td>2475.304550</td>
<td>2728.440120</td>
<td>0.15239</td>
</tr>
<tr>
<th>min</th>
<td>1001.000000</td>
<td>2023-01-01 00:00:00</td>
<td>100.120000</td>
<td>1.000000</td>
<td>60.280000</td>
<td>167.120000</td>
<td>0.00000</td>
</tr>
<tr>
<th>25%</th>
<td>1024.000000</td>
<td>2023-03-30 00:00:00</td>
<td>2550.297500</td>
<td>13.000000</td>
<td>1238.380000</td>
<td>1509.085000</td>
<td>0.08000</td>
</tr>
<tr>
<th>50%</th>
<td>1051.000000</td>
<td>2023-06-30 12:00:00</td>
<td>5019.300000</td>
<td>25.000000</td>
<td>2467.235000</td>
<td>2696.400000</td>
<td>0.15000</td>
</tr>
<tr>
<th>75%</th>
<td>1075.000000</td>
<td>2023-10-12 00:00:00</td>
<td>7507.445000</td>
<td>38.000000</td>
<td>3702.865000</td>
<td>3957.970000</td>
<td>0.23000</td>
</tr>
<tr>
<th>max</th>
<td>1100.000000</td>
<td>2024-01-01 00:00:00</td>
<td>9989.040000</td>
<td>49.000000</td>
<td>4995.300000</td>
<td>5442.150000</td>
<td>0.30000</td>
</tr>
<tr>
<th>std</th>
<td>29.573505</td>
<td>NaN</td>
<td>2846.790126</td>
<td>14.159006</td>
<td>1417.872546</td>
<td>1419.399839</td>
<td>0.08720</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h3 id="Check-if-Product_ID-has-unique-ranges-for-different-Product_Categories:">Check if Product_ID has unique ranges for different Product_Categories:<a class="anchor-link" href="#Check-if-Product_ID-has-unique-ranges-for-different-Product_Categories:"></a></h3>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">df3</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">'Product_ID'</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1050</span><span class="p">]</span>
<span class="n">df3</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>Product_ID</th>
<th>Sale_Date</th>
<th>Sales_Rep</th>
<th>Region</th>
<th>Sales_Amount</th>
<th>Quantity_Sold</th>
<th>Product_Category</th>
<th>Unit_Cost</th>
<th>Unit_Price</th>
<th>Customer_Type</th>
<th>Discount</th>
<th>Payment_Method</th>
<th>Sales_Channel</th>
<th>Region_and_Sales_Rep</th>
</tr>
</thead>
<tbody>
<tr>
<th>70</th>
<td>1050</td>
<td>2023-05-19</td>
<td>Charlie</td>
<td>East</td>
<td>9744.52</td>
<td>35</td>
<td>Clothing</td>
<td>2158.69</td>
<td>2384.38</td>
<td>Returning</td>
<td>0.09</td>
<td>Bank Transfer</td>
<td>Retail</td>
<td>East-Charlie</td>
</tr>
<tr>
<th>279</th>
<td>1050</td>
<td>2023-05-28</td>
<td>Alice</td>
<td>North</td>
<td>8086.27</td>
<td>6</td>
<td>Furniture</td>
<td>3763.26</td>
<td>4102.72</td>
<td>New</td>
<td>0.11</td>
<td>Credit Card</td>
<td>Retail</td>
<td>North-Alice</td>
</tr>
<tr>
<th>414</th>
<td>1050</td>
<td>2023-02-11</td>
<td>Charlie</td>
<td>West</td>
<td>1011.46</td>
<td>48</td>
<td>Furniture</td>
<td>710.06</td>
<td>851.35</td>
<td>Returning</td>
<td>0.04</td>
<td>Bank Transfer</td>
<td>Online</td>
<td>West-Charlie</td>
</tr>
<tr>
<th>548</th>
<td>1050</td>
<td>2023-06-01</td>
<td>Bob</td>
<td>South</td>
<td>5105.78</td>
<td>23</td>
<td>Furniture</td>
<td>3756.06</td>
<td>4255.73</td>
<td>Returning</td>
<td>0.04</td>
<td>Cash</td>
<td>Online</td>
<td>South-Bob</td>
</tr>
<tr>
<th>667</th>
<td>1050</td>
<td>2023-05-17</td>
<td>Bob</td>
<td>North</td>
<td>2254.91</td>
<td>45</td>
<td>Furniture</td>
<td>112.35</td>
<td>586.18</td>
<td>Returning</td>
<td>0.28</td>
<td>Credit Card</td>
<td>Retail</td>
<td>North-Bob</td>
</tr>
<tr>
<th>760</th>
<td>1050</td>
<td>2023-08-21</td>
<td>David</td>
<td>North</td>
<td>9976.52</td>
<td>17</td>
<td>Furniture</td>
<td>2346.80</td>
<td>2654.65</td>
<td>New</td>
<td>0.13</td>
<td>Cash</td>
<td>Retail</td>
<td>North-David</td>
</tr>
<tr>
<th>844</th>
<td>1050</td>
<td>2023-07-18</td>
<td>Eve</td>
<td>South</td>
<td>6107.78</td>
<td>43</td>
<td>Furniture</td>
<td>4834.47</td>
<td>4973.38</td>
<td>Returning</td>
<td>0.03</td>
<td>Bank Transfer</td>
<td>Online</td>
<td>South-Eve</td>
</tr>
<tr>
<th>865</th>
<td>1050</td>
<td>2023-03-05</td>
<td>Bob</td>
<td>North</td>
<td>9755.90</td>
<td>20</td>
<td>Electronics</td>
<td>3318.92</td>
<td>3785.91</td>
<td>New</td>
<td>0.24</td>
<td>Bank Transfer</td>
<td>Online</td>
<td>North-Bob</td>
</tr>
<tr>
<th>917</th>
<td>1050</td>
<td>2023-11-13</td>
<td>Alice</td>
<td>North</td>
<td>4638.47</td>
<td>28</td>
<td>Food</td>
<td>1711.63</td>
<td>1951.24</td>
<td>New</td>
<td>0.22</td>
<td>Cash</td>
<td>Online</td>
<td>North-Alice</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="Data-quality-insights-at-first-glance">Data quality insights at first glance<a class="anchor-link" href="#Data-quality-insights-at-first-glance"></a></h2>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<ul>
<li><p>The dataset consists of 1000 rows.</p>
</li>
<li><p>The data requires no cleaning - there are no missing values or duplicates.</p>
</li>
<li><p>Product_ID values are not unique across rows, nor are they unique per Product_Category. This would result in an innacurate product-based quantitative analysis.</p>
</li>
<li><p>Sales_Date contains a sufficient range of dates for time series analysis.</p>
</li>
<li><p>Dataset contains sufficient numerical data to perform various quantitative analyses.</p>
</li>
</ul>
</div>
</div>
</div>
</div>
<p>Let us now move on to <a href="../README.md#workflow-orchestration">orchestrating our pipeline</a><p>
</main>
</body>
</html>
