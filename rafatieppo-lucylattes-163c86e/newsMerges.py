lscsv_ldp = glob.glob('./csv_producao/*_ldp.csv')
dfldp = pd.DataFrame()
lsid = []
for i in range(len(lscsv_ldp)):
    a = pd.read_csv(lscsv_ldp[i], header=0)
    dfldp = dfldp.append(a, ignore_index=False)
    iid = fun_idd_unixwind(plat_sys, lscsv_ldp, i)
    idrep = np.repeat(iid, len(a['PESQUISA']))
    lsid.append(idrep)
dfldp['ID'] = np.concatenate(lsid)
lscsv_fullname = glob.glob('./csv_producao/*fullname.csv')
len(lscsv_fullname)
dffullname = pd.DataFrame()
for i in range(len(lscsv_fullname)):
    a = pd.read_csv(lscsv_fullname[i], header=0, dtype='str')
    dffullname = dffullname.append(a, ignore_index=False)
dfldp = pd.merge(dfldp, dffullname, on='ID')
dffullname = dffullname.reset_index(drop=True)
pathfilename = str('./csv_producao/ldp_all.csv')
dfldp.to_csv(pathfilename, index=False)
print(pathfilename, 'gravado com', len(dfldp['PESQUISA']), 'linhas de pesquisa')

