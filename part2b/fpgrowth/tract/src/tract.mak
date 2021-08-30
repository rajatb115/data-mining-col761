#-----------------------------------------------------------------------
# File    : tract.mak
# Contents: build item and transaction management (on Windows systems)
# Author  : Christian Borgelt
# History : 2008.10.05 file created from apriori makefile
#           2011.05.06 changed to double support reporting/recording
#           2011.08.29 main program fim16 added (mainly for testing)
#           2012.07.27 module tract with write functions added (trawr)
#           2013.04.04 added external modules and tract/train main prgs.
#           2016.04.20 completed dependencies on header files
#           2016.10.21 modules cm4seqs and cmfilter added (from coconad)
#-----------------------------------------------------------------------
THISDIR  = ..\..\tract\src
UTILDIR  = ..\..\util\src
MATHDIR  = ..\..\math\src

CC       = cl.exe
DEFS     = /D WIN32 /D NDEBUG /D _CONSOLE /D _CRT_SECURE_NO_WARNINGS
CFLAGS   = /nologo /W3 /O2 /GS- $(DEFS) /c $(ADDFLAGS)
INCS     = /I $(UTILDIR) /I $(MATHDIR)

LD       = link.exe
LDFLAGS  = /nologo /subsystem:console /incremental:no
LIBS     = 

HDRS_1   = $(UTILDIR)\fntypes.h    $(UTILDIR)\arrays.h     \
           $(UTILDIR)\symtab.h
HDRS_R	 = $(HDRS_1)               $(UTILDIR)\tabread.h
HDRS_W   = $(HDRS_1)               $(UTILDIR)\tabwrite.h
HDRS_RW  = $(HDRS_R)               $(UTILDIR)\tabwrite.h
HDRS_S   = $(HDRS_1)               $(UTILDIR)\scanner.h
HDRS     = $(HDRS_R)               $(UTILDIR)\error.h tract.h

OBJS     = $(UTILDIR)\arrays.obj   $(UTILDIR)\memsys.obj   \
           $(UTILDIR)\idmap.obj    $(UTILDIR)\escape.obj   \
           $(UTILDIR)\tabread.obj  $(UTILDIR)\tabwrite.obj \
           $(UTILDIR)\scform.obj \
           taread.obj patspec.obj clomax.obj repcm.obj

PSPOBJS  = $(UTILDIR)\arrays.obj   $(UTILDIR)\escape.obj   \
           $(UTILDIR)\idmap.obj    $(UTILDIR)\tabread.obj  \
           $(UTILDIR)\tabwrite.obj taread.obj train.obj

CMSOBJS  = $(UTILDIR)\arrays.obj   $(UTILDIR)\memsys.obj   \
           $(UTILDIR)\idmap.obj    $(UTILDIR)\escape.obj   \
           $(UTILDIR)\scform.obj   $(UTILDIR)\tabread.obj  \
           $(UTILDIR)\tabwrite.obj taread.obj trnread.obj  \
           patspec.obj clomax.obj repcm.obj cmsmain.obj

RGTOBJS  = $(UTILDIR)\arrays.obj   $(UTILDIR)\escape.obj   \
           $(UTILDIR)\idmap.obj    $(UTILDIR)\tabread.obj  \
           $(UTILDIR)\memsys.obj   $(UTILDIR)\scform.obj   \
           $(MATHDIR)\ruleval.obj  $(MATHDIR)\gamma.obj    \
           $(MATHDIR)\chi2.obj     taread.obj report.obj patspec.obj

PRGS     = fim16.exe tract.exe train.exe psp.exe rgt.exe

#-----------------------------------------------------------------------
# Build Programs
#-----------------------------------------------------------------------
all:          $(PRGS)

fim16.exe:    $(OBJS) ma16main.obj tract.mak
	$(LD) $(LDFLAGS) $(OBJS) m16main.obj $(LIBS) /out:$@

tract.exe:    $(OBJS) tramain.obj tract.mak
	$(LD) $(LDFLAGS) $(OBJS) tramain.obj $(LIBS) /out:$@

train.exe:    $(OBJS) trnmain.obj $(UTILDIR)\tabwrite.obj tract.mak
	$(LD) $(LDFLAGS) $(OBJS) $(UTILDIR)\tabwrite.obj \
              trnmain.obj $(LIBS) /out:$@

psp.exe:      $(PSPOBJS) pspmain.obj tract.mak
	$(LD) $(LDFLAGS) $(PSPOBJS) pspmain.obj $(LIBS) /Fo$@

rgt.exe:      $(RGTOBJS) rgmain.obj makefile
	$(LD) $(LDFLAGS) $(RGTOBJS) rgmain.obj $(LIBS) /Fo$@

#-----------------------------------------------------------------------
# Main Programs
#-----------------------------------------------------------------------
tramain.obj:  $(HDRS)
tramain.obj:  tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_MAIN tract.c /Fo$@

trnmain.obj:  $(HDRS) $(UTILDIR)\random.h $(UTILDIR)\tabwrite.h
trnmain.obj:  train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TRN_MAIN train.c /Fo$@

m16main.obj:  $(HDRS) $(UTILDIR)\memsys.h report.h clomax.h
m16main.obj:  fim16.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D M16_MAIN fim16.c /Fo$@

pspmain.obj:  $(HDRS) $(UTILDIR)\tabwrite.h
pspmain.obj:  patspec.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D PSP_MAIN patspec.c /Fo$@

cmsmain.obj:  $(HDRS_1) $(UTILDIR)\memsys.h tract.h report.h
cmsmain.obj:  cm4seqs.h cm4seqs.c makefile
	$(CC) $(CFLAGS) $(INCS) /D CMS_MAIN cm4seqs.c /Fo$@

rgmain.obj:   $(HDRS) $(UTILDIR)\memsys.h $(MATHDIR)\ruleval.h report.h
rgmain.obj:   rulegen.c makefile
	$(CC) $(CFLAGS) $(INCS) /D RG_MAIN rulegen.c /Fo$@

#-----------------------------------------------------------------------
# Item and Transaction Management
#-----------------------------------------------------------------------
tract.obj:    $(HDRS_1)
tract.obj:    tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) tract.c /Fo$@

tasurr.obj:   $(HDRS_1) $(UTILDIR)\random.h
tasurr.obj:   tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_SURR tract.c /Fo$@

taread.obj:   $(HDRS_R)
taread.obj:   tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_READ tract.c /Fo$@

tarw.obj:     $(HDRS_RW)
tarw.obj:     tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_READ /D TA_WRITE tract.c /Fo$@

tars.obj:     $(HDRS_R) $(UTILDIR)\random.h
tars.obj:     tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_READ /D TA_SURR tract.c /Fo$@

tard.obj:     $(HDRS_R)
tard.obj:     tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_READ /D SUPP=double tract.c /Fo$@

tatree.obj:   $(HDRS_R)
tatree.obj:   tract.h tract.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TA_READ /D TATREEFN tract.c /Fo$@

#-----------------------------------------------------------------------
# Train Management
#-----------------------------------------------------------------------
train.obj:    $(HDRS_1) tract.h
train.obj:    train.h train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) train.c /Fo$@

trnsurr.obj:  $(HDRS_1) $(UTILDIR)\random.h tract.h
trnsurr.obj:  train.h train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TRN_SURR train.c /Fo$@

trnread.obj:  $(HDRS_R) tract.h
trnread.obj:  train.h train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TRN_READ train.c /Fo$@

trnrw.obj:    $(HDRS_RW) tract.h
trnrw.obj:    train.h train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TRN_READ /D TRN_WRITE train.c /Fo$@

trnrs.obj:    $(HDRS_R) $(UTILDIR)\random.h tract.h
trnrs.obj:    train.h train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TRN_READ /D TRN_SURR train.c /Fo$@

trnrd.obj:    $(HDRS_R) tract.h
trnrd.obj:    train.h train.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D TRN_READ /D SUPP=double \
              train.c /Fo$@

#-----------------------------------------------------------------------
# Frequent Item Set Mining (with at most 16 items)
#-----------------------------------------------------------------------
fim16.obj:    $(HDRS)
fim16.obj:    fim16.c tract.mak
	$(CC) $(CFLAGS) $(INCS) fim16.c /Fo$@

#-----------------------------------------------------------------------
# Pattern Statistics Management
#-----------------------------------------------------------------------
patspec.obj:  $(HDRS_W)
patspec.obj:  patspec.h patspec.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D PSP_REPORT patspec.c /Fo$@

pspdbl.obj:   $(HDRS_W)
pspdbl.obj:   patspec.h patspec.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D SUPP=double /D PSP_REPORT \
              patspec.c /Fo$@

pspest.obj:   $(HDRS_W) $(UTILDIR)\random.h $(MATHDIR)\gamma.h
pspest.obj:   patspec.h patspec.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D PSP_REPORT /D PSP_ESTIM \
	      patspec.c /Fo$@

pspetr.obj:   $(HDRS_W) $(UTILDIR)\random.h $(MATHDIR)\gamma.h
pspetr.obj:   patspec.h patspec.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D PSP_REPORT /D PSP_ESTIM /D PSP_TRAIN \
              patspec.c /Fo$@

#-----------------------------------------------------------------------
# Prefix Tree Management for Closed/Maximal Filtering
#-----------------------------------------------------------------------
clomax.obj:   $(HDRS_1) $(UTILDIR)\memsys.h tract.h
clomax.obj:   clomax.h clomax.c tract.mak
	$(CC) $(CFLAGS) $(INCS) clomax.c /Fo$@

cmdbl.obj:    $(HDRS_1) $(UTILDIR)\memsys.h tract.h
cmdbl.obj:    clomax.h clomax.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D RSUPP=double clomax.c /Fo$@

#-----------------------------------------------------------------------
# Prefix Tree Management for Closed and Maximal Permutations
#-----------------------------------------------------------------------
cm4seqs.obj:  $(HDRS) $(UTILDIR)\memsys.h tract.h report.h
cm4seqs.obj:  cm4seqs.h cm4seqs.c makefile
	$(CC) $(CFLAGS) $(INCS) cm4seqs.c /Fo$@

#-----------------------------------------------------------------------
# Linear Closed/Maximal Filter Management
#-----------------------------------------------------------------------
cmfilter.obj: $(HDRS) tract.h report.h
cmfilter.obj: cmfilter.c makefile
	$(CC) $(CFLAGS) $(INCS) cmfilter.c /Fo$@

cmfdbl.obj:   $(HDRS) tract.h report.h
cmfdbl.obj:   cmfilter.c makefile
	$(CC) $(CFLAGS) $(INCS) /D RSUPP=double cmfilter.c /Fo$@

#-----------------------------------------------------------------------
# Item Set Reporter Management
#-----------------------------------------------------------------------
report.obj:   $(HDRS_S) tract.h patspec.h
report.obj:   report.h report.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D ISR_PATSPEC report.c /Fo$@

repdbl.obj:   $(HDRS_S) tract.h patspec.h
repdbl.obj:   report.h report.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D RSUPP=double /D ISR_PATSPEC \
              report.c /Fo$@

repcm.obj:    $(HDRS_S) tract.h patspec.h clomax.h
repcm.obj:    report.h report.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D ISR_PATSPEC /D ISR_CLOMAX \
              report.c /Fo$@

repcmd.obj:   $(HDRS_S) tract.h patspec.h clomax.h
repcmd.obj:   report.h report.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D RSUPP=double /D ISR_PATSPEC \
              /D ISR_CLOMAX report.c /Fo$@

#-----------------------------------------------------------------------
# Rule Generation Tree Management
#-----------------------------------------------------------------------
rulegen.obj:  $(HDRS_1) $(UTILDIR)\memsys.h $(MATHDIR)\ruleval.h tract.h
rulegen.obj:  rulegen.h rulegen.c tract.mak
	$(CC) $(CFLAGS) $(INCS) rulegen.c /Fo$@

rgrfn.obj:    $(HDRS_1) $(UTILDIR)\memsys.h $(MATHDIR)\ruleval.h tract.h
rgrfn.obj:    rulegen.h rulegen.c tract.mak
	$(CC) $(CFLAGS) $(INCS) /D RG_REPOFN rulegen.c /Fo$@

#-----------------------------------------------------------------------
# Pattern Set Reduction
#-----------------------------------------------------------------------
patred.obj:   $(HDRS_1) tract.h report.h
patred.obj:   patred.h patred.c makefile
	$(CC) $(CFLAGS) $(INCS) patred.c /Fo$@

#-----------------------------------------------------------------------
# External Modules
#-----------------------------------------------------------------------
$(UTILDIR)\arrays.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak arrays.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\memsys.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak memsys.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\idmap.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak idmap.obj    ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\escape.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak escape.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\tabread.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak tabread.obj  ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\tabwrite.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak tabwrite.obj ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(UTILDIR)\scform.obj:
	cd $(UTILDIR)
	$(MAKE) /f util.mak scform.obj   ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(MATHDIR)\ruleval.obj:
	cd $(MATHDIR)
        $(MAKE) /f math.mak ruleval.obj  ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(MATHDIR)\gamma.obj:
	cd $(MATHDIR)
        $(MAKE) /f math.mak gamma.obj    ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)
$(MATHDIR)\chi2.obj:
	cd $(MATHDIR)
        $(MAKE) /f math.mak gamma.obj    ADDFLAGS="$(ADDFLAGS)"
	cd $(THISDIR)

#-----------------------------------------------------------------------
# Clean up
#-----------------------------------------------------------------------
localclean:
	-@erase /Q *~ *.obj *.idb *.pch $(PRGS)

clean:
	$(MAKE) /f tract.mak localclean
	cd $(MATHDIR)
	$(MAKE) /f math.mak clean
	cd $(UTILDIR)
	$(MAKE) /f util.mak clean
	cd $(THISDIR)
