import pandas as pd
def prep_data(df):

	df = (df\
	.assign(hw=df["Height"] * df["Width"])\
	.assign(l1_l2 = df["Length1"]*df["Length2"])\
	.assign(l1_l3 = df["Length1"]*df["Length3"])\
	.assign(l2_l3 = df["Length2"]*df["Length3"])\
	.assign(l1_sq = df["Length1"]**2)\
	.assign(l2_sq = df["Length2"]**2)\
	.assign(l3_sq = df["Length3"]**2)\
	.assign(abs_diff_l1_l2 = (df["Length1"]-df["Length2"]).abs())\
	.assign(abs_diff_l1_l3 = (df["Length1"]-df["Length3"]).abs())\
	.assign(abs_diff_l2_l3 = (df["Length2"]-df["Length3"]).abs())\
	.merge(pd.get_dummies(df.Species), left_index=True, right_index=True)
		 )
# 	df = df.merge(pd.get_dummies(df.Species), left_index=True, right_index=True)
	# 	df = df.assign(hw=df["Height"] * df["Width"])

	
	X = df.loc[:, (df.columns != "Weight") & (df.columns != "Species")].values
	y = df["Weight"].values

	return X, y

