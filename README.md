# ChillingEffect
This is the course project for CSE534

Chilling Effects (https://www.chillingeffects.org), started from 2001, is an independent third party research project studying cease and desist let- ters concerning online content. It is launched and main- tained by the Berkman Center for Internet & Society, Har- vard University. The website collects and manages com- plaints about online activities, especially requests (or no- tices) to remove content from online.

As far as we know, there are no existing literature focus- ing on the data analysis of Chilling Effect. Thus the prob- lems are not well defined. Based on our preliminary analy- sis on the dataset, we find that there are abundant of tem- poral anomalies, i.e. the amount of notices sent from or to an entity suddenly increases by a significant amount. Such anomalies are interesting. Why do they occur? Are they driven by incidents in real world? How can we use these information to better understand the dataset?

In the light of these questions, we explored the Chilling Effect Dataset with various data mining and visualization techniques. We also observed interesting connections be- tween the data and real world events. The major contribu- tions of this work are:

• We discover an interesting phenomenon in Chilling Effect Dataset: there are plenty of temporal anoma- lies in the time series of notices from one sender to one recipient (i.e. time series of all notices between sender-recipient pairs).

• We propose a novel method to automatically detect temporal anomalies in time series and visualize cor- responding topics for sense making. Besides auto- matic method, we also design and implement con- venient interactive interface for manual inspection.

• We conduct plenty of case studies to validate the ef- fectiveness of our method. For brevity, we only present the most interesting ones in the report.

• We share our codes on Github[URL] for future use.
