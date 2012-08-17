from django.db import models

# Create your models here.
class Regimen(models.Model):
    name = models.CharField(max_length=40)
    shortcut = models.CharField(max_length=20)
    description = models.TextField()
    def __unicode__(self):
        return self.shortcut

class Lifespan(models.Model):
    name = models.CharField(max_length=40)
    shortcut = models.CharField(max_length=20)
    def __unicode__(self):
        return self.shortcut


class Reference(models.Model):
    pmid = models.IntegerField(blank=True, null=True) #) # 
    title = models.CharField(max_length=250, blank=True)
    authors = models.TextField(blank=True)  #models.ManyToManyField(Author) max_length=250, 
    keywords = models.CharField(max_length=250, blank=True)
    link = models.URLField(blank=True)
    url = models.URLField(blank=True)
    journal = models.CharField(max_length=250, blank=True)
    year = models.IntegerField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    issue = models.CharField(max_length=10, blank=True) # Was Integer, but encounterd "2-3" value!
    pages = models.CharField(max_length=10, blank=True)
    start_page = models.IntegerField(blank=True, null=True)
    epub_date = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    type_of_article = models.CharField(max_length=10, blank=True)
    short_title = models.CharField(max_length=50, blank=True)
    alternate_journal = models.CharField(max_length=150, blank=True)
    issn = models.IntegerField(blank=True, null=True)
    doi = models.CharField(max_length=30,blank=True)
    original_publication = models.CharField(max_length=100, blank=True)
    reprint_editione = models.CharField(max_length=100, blank=True)
    reviewed_itemse = models.CharField(max_length=100, blank=True)
    legal_note = models.CharField(max_length=100, blank=True)
    pmcid = models.IntegerField(blank=True, null=True)
    nihmsid = models.IntegerField(blank=True, null=True)
    article_number = models.IntegerField(blank=True, null=True)
    accession_number = models.IntegerField(blank=True, null=True)
    call_number = models.IntegerField(blank=True, null=True)
    label = models.CharField(max_length=100, blank=True)
    notes = models.CharField(max_length=100, blank=True)    # Make it to a ManyToManyField.
    research_notes = models.CharField(max_length=100, blank=True) # dito.
    #file_attachment = models.FileField(blank=True)
    author_address = models.CharField(max_length=150, blank=True)
    #figure = models.ImageField(blank=True)
    caption = models.CharField(max_length=100, blank=True)
    access_date = models.DateField(blank=True, null=True)
    translated_author = models.CharField(max_length=100, blank=True)
    name_of_database = models.CharField(max_length=100, blank=True)
    database_provider = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    class Meta():
        db_table = u'reference'        
    
    def __repr__(self):
        if self.authors and self.title:
            authors = self.authors.split('; ')
            if len(authors) == 1:
                representation = "%s, %s" %(authors[0], self.year)
            elif len(authors) == 2:
                representation = "%s & %s, %s" % (authors[0], authors[1], self.year)
            else:
                representation = "%s et al., %s" %(authors[0], self.year)
            return "%s %s" % (representation, self.title)
        elif self.title:
            return self.title
        else:
            return self.pmid
    
    def __unicode__(self):
        return "%s" % self.pmid


class Signature(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    symbol = models.CharField(max_length=30, blank=True)
    exp = models.FloatField(blank=True)
    ctr = models.FloatField(blank=True)
    fold_change = models.FloatField(blank=True)
    p_value = models.FloatField(blank=True)
    experimental = models.CharField(max_length=30, blank=True)
    control = models.CharField(max_length=30, blank=True)
    tissue = models.CharField(max_length=30, blank=True)
    age = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=50, blank=True)
    def __unicode__(self):
        return self.symbol

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first.name, self.last_name)

class Manipulation(models.Model):
    shortcut = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    type = models.ManyToManyField('self', symmetrical=False, related_name='type_of', blank=True)
    #type = models.ManyToManyField('self', through='ManipulationType', symmetrical=False, related_name='type_of', blank=True)

##    def add_manipulation_type(self, manipulation):
##        relationship
    
    def __unicode__(self):
        return self.name
    
    class Meta():
        db_table = u'manipulation'

##class ManipulationType(models.Model):
##    from_manipulation = models.ForeignKey(Manipulation, related_name='from_manipulation')
##    to_manipulation = models.ForeignKey(Manipulation, related_name='to_manipulation')
##
##    class Meta():
##        db_table = u'manipulation_type'
##        

class Intervention(models.Model):
    name = models.CharField(max_length=250)
    taxid = models.IntegerField(blank=True, null=True)
    background = models.CharField(max_length=250, blank=True)
    sex = models.CharField(max_length=25, blank=True)
    lifespans = models.CharField(max_length=25, blank=True)
    effect = models.TextField(blank=True)
    mean = models.CharField(max_length=15, null=True, blank=True)
    median = models.CharField(max_length=15, null=True, blank=True)
    _25 = models.CharField(max_length=15, null=True, blank=True)
    _75 = models.CharField(max_length=15, null=True, blank=True)
    maximum = models.CharField(max_length=15, null=True, blank=True)
    pmid = models.CharField(max_length=250, blank=True)
    references = models.ManyToManyField(Reference, blank=True)
    manipulation = models.ManyToManyField(Manipulation, blank=True)
    
##    species = models.ManyToManyField(Species)
    def __unicode__(self):
        return self.name


class Gendr(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    ensembl_gene_id = models.CharField(max_length=18, blank=True)
    gene_symbol = models.CharField(max_length=13, blank=True)
    gene_name = models.CharField(max_length=150, blank=True)
    alias = models.CharField(max_length=50, blank=True)
    function = models.CharField(max_length=500, blank=True)
    observation = models.TextField(blank=True)
    classification = models.CharField(max_length=10)
    regimen = models.ManyToManyField(Regimen)
    lifespan = models.ManyToManyField(Lifespan)
    taxid = models.IntegerField()
    pubmed_id = models.CharField(max_length=87, blank=True)
    reference = models.CharField(max_length=250, blank=True)

    def __unicode__(self):
        return self.gene_symbol
##    def get_fields(self):
##        #make a list of field/values.
##        return [(field, field.value_to_string(self)) for field in Gendr._meta.fields]
    @property
    def lifespans(self):
        return Lifespan.objects.filter(gendr__lifespan=self).all()


class Type(models.Model):
    name = models.CharField(max_length=25)
    def __unicode__(self):
        return self.name


class GenAge(models.Model):  # Rename to Entity AgeFactor
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    #geneid = models.ForeignKey(Gene, blank=True)   # Or Genes
    mapping = models.IntegerField(null=True, blank=True)
    ensembl_gene_id = models.CharField(max_length=18, blank=True)
    symbol = models.CharField(max_length=13, blank=True)   # Rename to symbol.
    name = models.CharField(max_length=244, blank=True)    # Rename to name.
    alias = models.CharField(max_length=270, blank=True)
    function = models.TextField(blank=True)    # Manually curated functional description field.
    description = models.TextField(blank=True) # Automatically populated field for functional descriptions.
    functional_description = models.TextField(blank=True)    
    observation = models.TextField(blank=True)
    classification = models.CharField(max_length=20, blank=True)
    classifications = models.ManyToManyField('annotations.Classification')
    regimen = models.ManyToManyField(Regimen, blank=True)
    lifespan = models.ManyToManyField(Lifespan)
    diet_regimen = models.CharField(max_length=250, blank=True)
    life_span = models.CharField(max_length=250, blank=True)   
    taxid = models.IntegerField(null=True, blank=True)
    #species = models.ManyToManyField(Taxonomy)
    pubmed_id = models.CharField(max_length=250, blank=True)
    reference = models.CharField(max_length=250, blank=True)
    references = models.ManyToManyField(Reference, blank=True)
    mean = models.CharField(max_length=15, null=True, blank=True)
    median = models.CharField(max_length=15, null=True, blank=True)
    maximum = models.CharField(max_length=15, null=True, blank=True)
    _75 = models.CharField(max_length=15, null=True, blank=True)
    _25 = models.CharField(max_length=15, null=True, blank=True)
    manipulation = models.CharField(max_length=250, null=True, blank=True)
    intervention = models.ManyToManyField(Intervention, blank=True)
    gene_intervention = models.CharField(max_length=250, null=True, blank=True)
    synergistic_epistasis = models.CharField(max_length=33, blank=True)
    antagonistic_epistasis = models.CharField(max_length=216, blank=True)
    human_homologue = models.CharField(max_length=18, blank=True)
    note = models.CharField(max_length=250, null=True, blank=True)
    type = models.CharField(max_length=25, null=True, blank=True) # Gene, or drug
    types = models.ManyToManyField(Type, blank=True)
    
    
    def __unicode__(self):
        return self.symbol

    def data(self):
        return self.entrez_gene_id, self.symbol, self.name, self.alias

    data = property(data)

class Change(models.Model):
    name = models.CharField(max_length=250)
    taxid = models.IntegerField(null=True, blank=True)
    reference = models.CharField(max_length=250, null=True, blank=True)
    pmid = models.IntegerField(null=True, blank=True)
    tissue = models.CharField(max_length=250, null=True, blank=True)
    comparision = models.CharField(max_length=250, null=True, blank=True)
    start = models.CharField(max_length=250, null=True, blank=True)
    stop = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=25, blank=True)
    description = models.TextField(blank=True)
    references = models.ManyToManyField(Reference, blank=True)
    description = models.TextField(max_length=250, blank=True)
    def __repr__(self):
        return self.name


class GenCC(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    gene_symbol = models.CharField(max_length=13, blank=True)
    alias = models.CharField(max_length=68, blank=True)
    taxid = models.IntegerField()
    function = models.CharField(max_length=255, blank=True)
    observation = models.CharField(max_length=248, blank=True)
    pubmed_id = models.IntegerField(null=True, blank=True)
    reference = models.CharField(max_length=37, blank=True)
    classification = models.CharField(max_length=5)
    peak_mrna = models.CharField(max_length=5, blank=True)
    peak_protein = models.CharField(max_length=5, blank=True)
    peak_actvity = models.CharField(max_length=5, blank=True)
    procession = '''
    Identified entrez_gene_id 22339 for gene_symbol Vegf via Alias alias.
    Pp2a mapped to multiple genes via Alias alias.
    '''  
    def __unicode__(self):
        return self.gene_symbol

class AdultHeightAssociation(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    locus_rank = models.IntegerField()
    chr = models.CharField(max_length=5)
    gene_symbol = models.CharField(max_length=8)
    snp = models.CharField(max_length=10)
    effect_allele = models.CharField(max_length=1)
    male_effect = models.CharField(max_length=1)
    male_p = models.FloatField()
    female_effect = models.CharField(max_length=1)
    female_p = models.FloatField()
    phet_m_vs_f = models.FloatField()
    taxid = 9606

class CircadianSystemicEntrainedFactors(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    gene_symbol = models.CharField(max_length=13)
    alias = models.CharField(max_length=13, blank=True)
    taxid = 10090
    classification = 'CS'
    def __unicode__(self):
        return self.gene_symbol

class ClockModulator(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    confirmed_by_bmal1_kockdown = models.CharField(max_length=10)
    gene_symbol = models.CharField(max_length=9)
    rna_nucleotide_accession_version = models.CharField(max_length=12)
    gene_name = models.CharField(max_length=152)
    phenotype = models.CharField(max_length=30)
    classification = models.CharField(max_length=8)
    taxid = 9606
    processing = '''
    14.01.2011 Converted Disconected Ids to current_entrez_gene_ids via mapping10.py:
    Changed Gene CDC2L1 in Dataset Zhang2009 from 442766 to 984
    Changed Gene CMYA4 in Dataset Zhang2009 from 191583 to 146862
    Changed Gene HRPT2 in Dataset Zhang2009 from 3279 to 79577
    Changed Gene ZNF261 in Dataset Zhang2009 from 442790 to 9203
    Changed Gene WDR9 in Dataset Zhang2009 from 379039 to 54014
    22.01.2011 41 of 394 genes were not mapped to entrez gene id and 2 mapped to multiple
    secondary mapping left 6 genes as unmapped
    Mannually mapping:
    Record removed. NM_182831.1: This RefSeq was permanently suppressed because currently there is support for the transcript but not for the protein.
    --> gene_symbol = 'C16orf82' --> entrez_gene_id = 162083; alias = 'TNT'; other = "Protein TNT"

    NM_020755 --> entrez_gene_id = 57515; alias = 'TDE2'; other_designation = 'tumor differentially expressed 2'

    
    used Rna nucleotide accession version with __startwith clausal to map the remaining 4
    '''
    
class HumanGenes(models.Model):
    mapping = models.IntegerField(null=True, blank=True)
    hagrid = models.IntegerField()
    gene_symbol = models.CharField(max_length=8)
    gene_name = models.CharField(max_length=131)
    aliases = models.CharField(max_length=68, blank=True)
    epd_accession = models.CharField(max_length=11, blank=True)
    orf_accession = models.CharField(max_length=12)
    cds_accession = models.CharField(max_length=12, blank=True)
    selection_reason = models.CharField(max_length=21)
    band = models.CharField(max_length=10)
    location_start = models.IntegerField()
    location_end = models.IntegerField()
    orientation = models.IntegerField()
    function = models.CharField(max_length=94)
    cellular_location = models.CharField(max_length=40)
    expression = models.CharField(max_length=69)
    observations = models.TextField()
    omim = models.IntegerField()
    hprd = models.IntegerField()
    unigene = models.IntegerField()
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    homologene = models.IntegerField()
    swiss_prot = models.CharField(max_length=11, blank=True)
    interactions = models.TextField(blank=True)
    homologues = models.TextField()
    reference = models.TextField()
    pubmed_ids = models.TextField()
    taxid = 9606
    classification = 'AA'
    def __unicode__(self):
        return self.gene_symbol

class JoanneGenes(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    gene_symbol = models.CharField(max_length=8)
    ensembl_gene_id = models.CharField(max_length=16)
    dn = models.FloatField()
    ds = models.FloatField()
    dn_ds = models.FloatField()
    human_percentage_id = models.IntegerField()
    chimp_percentage_id = models.IntegerField()
    chimp_ensembl_gene_id = models.CharField(max_length=19)
    assoc_gene_name = models.CharField(max_length=8)
    cds_length = models.IntegerField()
    longevity = models.CharField(max_length=18)
    taxid = 9606
    classification = 'LA'
    def __unicode__(self):
        return self.gene_symbol

class MurineImprinted(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    gene_symbol = models.CharField(max_length=9)
    chromosome = models.CharField(max_length=4)
    chromosome_region = models.CharField(max_length=7)
    expressed_parental_allele = models.CharField(max_length=1)
    gene_name = models.CharField(max_length=74)
    classification = models.CharField(max_length=5)
    taxid = 10090

class NewLongevityRegulators(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    wormbase_id = models.CharField(max_length=14)
    phenotype = models.CharField(max_length=11)
    classification = models.CharField(max_length=2)
    taxid = 6239
    def __unicode__(self):
        return self.wormbase_id

class NewLongevityRegulatorsCandidates(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    wormbase_id = models.CharField(max_length=14, blank=True)
    gene_symbol = models.CharField(max_length=9, blank=True)
    ensembl_gene_id = models.CharField(max_length=11)
    taxid = 6239
    def __unicode__(self):
        return self.gene_symbol

class SurvivingInTheCold(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    locus_tag = models.CharField(max_length=10)
    protein_accession_number = models.CharField(max_length=10)
    sgd_id = models.CharField(max_length=10)
    embl = models.CharField(max_length=6)
    taxid = 4932
    classification = 'PG'
    def __unicode__(self):
        return self.locus_tag

class HumanBrainDnaMethylationChanges(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=10)
    chr = models.IntegerField()
    genomic_position_in_bp = models.IntegerField()
    gene_symbol = models.CharField(max_length=7)
    distance_to_tss = models.IntegerField()
    stage_i_pvalue_crblm = models.FloatField()
    stage_i_pvalue_fctx = models.FloatField()
    stage_i_pvalue_pons = models.FloatField()
    stage_i_pvalue_tctx = models.FloatField()
    stage_ii_pvalue_crblm = models.FloatField()
    stage_ii_pvalue_fctx = models.FloatField()
    beta_coefficient_range = models.CharField(max_length=13)
    adjusted_r2_estimates_from_stage_i_crblm = models.FloatField()
    adjusted_r2_estimates_from_stage_i_fctx = models.FloatField()
    adjusted_r2_estimates_from_stage_i_pons = models.FloatField()
    adjusted_r2_estimates_from_stage_i_tctx = models.FloatField()
    cpg_sequence = models.TextField(blank=True)
    size = models.CharField(max_length=4)
    cpg_count = models.CharField(max_length=4)
    c_g_count = models.CharField(max_length=4)
    percentage_cpg = models.CharField(max_length=4)
    percentage_c_or_g = models.CharField(max_length=4)
    ratio = models.CharField(max_length=4)
    cpg_sequence_2kb = models.TextField(blank=True)
    taxid = 9606
    classification = 'AM'

class K56Ac(models.Model):
    ensembl_gene = models.CharField(max_length=9, primary_key = True)
    level = models.FloatField()
    expression = models.FloatField()
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    taxid = 4932
    pmid = 15882620 


class Pokholok(models.Model):
    ensembl_gene = models.CharField(max_length=19)
    chr = models.IntegerField()
    pos = models.IntegerField()
    h3_ypd = models.FloatField(blank=True)
    h4_ypd = models.FloatField(blank=True)
    h3_h2o2 = models.FloatField(blank=True)
    h3k9acvsh3_ypd = models.FloatField(blank=True)
    h3k14acvsh3_ypd = models.FloatField(blank=True)
    h3k14acvswce_ypd = models.FloatField(blank=True)
    h3k14acvsh3_h2o2 = models.FloatField(blank=True)
    h4acvsh3_ypd = models.FloatField(blank=True)
    h4acvsh3_h2o2 = models.FloatField(blank=True)
    h3k4me1vsh3_ypd = models.FloatField(blank=True)
    h3k4me2vsh3_ypd = models.FloatField(blank=True)
    h3k4me3vsh3_ypd = models.FloatField(blank=True)
    h3k36me3vsh3_ypd = models.FloatField(blank=True)
    h3k79me3vsh3_ypd = models.FloatField(blank=True)
    esa1_ypd = models.FloatField(blank=True)
    gcn5_ypd = models.FloatField(blank=True)
    gcn4_aa = models.FloatField(blank=True)
    gg_ypd = models.FloatField(blank=True)
    noab_ypd = models.FloatField(blank=True)
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    taxid = 4932
    pmid = 16122420

class Acetylation(models.Model):
    ensembl_gene = models.CharField(max_length=9, primary_key=True)
    h4k8 = models.FloatField()
    h4k12 = models.FloatField()
    h4k16 = models.FloatField()
    h3k9 = models.FloatField()
    h3k14 = models.FloatField()
    h3k18 = models.FloatField()
    h3k23 = models.FloatField()
    h3k27 = models.FloatField()
    h2ak7 = models.FloatField()
    h2bk11 = models.FloatField()
    h2bk16 = models.FloatField()
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    taxid = 4932
    pmid = 15186774

class HumanBrainMethylationChanges(models.Model):
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=10)
    chr = models.IntegerField()
    genomic_position_in_bp = models.IntegerField()
    symbol = models.CharField(max_length=8)
    distance_to_tss = models.IntegerField()
    stage_i_p_value_crblm = models.FloatField()
    stage_i_p_value_fctx = models.FloatField()
    stage_i_p_value_pons = models.FloatField()
    stage_i_p_value_tctx = models.FloatField()
    stage_ii_p_value_crblm = models.FloatField()
    stage_ii_p_value_fctx = models.FloatField()
    beta_coefficient_range = models.CharField(max_length=24)
    adjusted_r2_estimates_from_stage_i_crblm = models.FloatField()
    adjusted_r2_estimates_from_stage_i_fctx = models.FloatField()
    adjusted_r2_estimates_from_stage_i_pons = models.FloatField()
    adjusted_r2_estimates_from_stage_i_tctx = models.FloatField()
    cpg_sequence = models.TextField(blank=True)
    size = models.CharField(max_length=4)
    cpg_count = models.CharField(max_length=4)
    c_g_count = models.CharField(max_length=4)
    percentage_cpg = models.CharField(max_length=4)
    percentage_c_or_g = models.CharField(max_length=4)
    ratio = models.CharField(max_length=4)
    cpg_sequence_2kb = models.TextField(blank=True)
    taxid = 9606
    classification = 'AM' 
    def __unicode__(self):
        return self.symbol

class OneyrCbSpecific(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=15)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'cerebrellum'
    age = '1 year'
    
class OneyrHippSpecific(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=14)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'hippocampus'
    age = '1 year'
    
class AdultCbDynamic(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=14)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'cerebrellum'
    age = '6 weeks'
    
class AdultCbStable(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=15)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'cerebrellum'
    age = '6 weeks'
    
class AdultHippDynamic(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=14)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'hippocampus'
    age = '6 weeks'
    
class AdultHippStable(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=15)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'hippocampus'
    age = '6 weeks'
    
class CbSpecific(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=15)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'cerebrellum'
    
class HippSpecific(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=15)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'hippocampus'

class P7CbDynamic(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=15)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'cerebrellum'
    age = 'P7'
    
class P7HippDynamic(models.Model):
    chr = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    peak = models.CharField(max_length=14)
    p_value = models.FloatField()
    seq = models.TextField()
    gene = models.IntegerField()
    taxid = 9606
    tissue = 'hippocampus'
    age = 'P7'

class Ultradian(models.Model):
    orf = models.CharField(max_length=7)
    gene = models.CharField(max_length=5)
    description = models.CharField(max_length=243)
    process = models.CharField(max_length=225,blank=True)
    component = models.CharField(max_length=65,blank=True)
    function = models.CharField(max_length=165,blank=True)
    f = models.IntegerField()
    o = models.FloatField(blank=True)

class Adult_Height_Association(models.Model):
    locus_rank = models.IntegerField()
    chr = models.CharField(max_length=5)
    gene_symbol = models.CharField(max_length=8)
    snp = models.CharField(max_length=10)
    effect_allele = models.CharField(max_length=1)
    male_effect = models.CharField(max_length=1)
    male_p = models.FloatField()
    female_effect = models.CharField(max_length=1)
    female_p = models.FloatField()
    phet_m_vs_f = models.FloatField()
    taxid = 9606
    classification = 'JA'
    def __unicode__(self):
        return self.gene_symbol

class BMAL1_Sites_Liver(models.Model):
    chromosome = models.CharField(max_length=5)
    start = models.IntegerField()
    end = models.IntegerField()
    distance = models.IntegerField()
    gene_symbol = models.CharField(max_length=18)
    biotype = models.CharField(max_length=23)
    mrna_pvalue = models.FloatField()
    mrna_phase = models.FloatField()
    e1 = models.IntegerField()
    e1_e2 = models.IntegerField()
    conservation = models.FloatField()
    zt2 = models.IntegerField()
    zt6 = models.IntegerField()
    zt10 = models.IntegerField()
    zt14 = models.IntegerField()
    zt18 = models.IntegerField()
    zt22 = models.IntegerField()
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    mapping = models.IntegerField(null=True, blank=True)
    taxid = 10090
    tissue = 'liver'

class DAM_Fernandez2011(models.Model):
    cpg_site = models.CharField(max_length=19)
    cgi = models.CharField(max_length=1)
    gene_symbol = models.CharField(max_length=11)
    correlation = models.FloatField()
    p_value = models.FloatField()


class DR_Essential(models.Model):
    taxid = models.IntegerField()
    classification = models.CharField(max_length=10)
    entrez_gene_id = models.IntegerField(null=True, blank=True)
    gene_symbol = models.CharField(max_length=30)