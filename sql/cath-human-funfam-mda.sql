select distinct
  u.uniprot_acc as uniprot_acc,
  ff.member_id as domain_id,
  ff.member_type as domain_type,
  u.gene_name as gene_name,
  u.gene_id as gene_id,
  ff.superfamily_id as superfamily_id,
  ff.superfamily_id || '-ff-' || ff.funfam_number as funfam_id,
  mda.mda as mda,
  u.description as description
from
  {tablespace}.uniprot_description u,
  {tablespace}.funfam_member ff,
  {tablespace}.mda mda
where
  ff.sequence_md5 = u.sequence_md5
  and
  ff.sequence_md5 = mda.sequence_md5
  and
  u.taxon_id = 9606
