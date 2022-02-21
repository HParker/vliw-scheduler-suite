make;

mkdir -p submission

cp Makefile submission
cp *.cpp submission
cp *.h submission

echo "- source order"
./vliwScheduler simple.s submission/4_wide_source_simple.s 0
echo "- critical path"
./vliwScheduler simple.s submission/4_wide_critpath_source_simple.s 1
echo "- resource order"
./vliwScheduler simple.s submission/4_wide_resource_source_simple.s 2
echo "- fanout"
./vliwScheduler simple.s submission/4_wide_fanout_source_simple.s 3
echo "- critical path resource tiebreaker"
./vliwScheduler simple.s submission/4_wide_critpath_resource_source_simple.s 4
echo "- critical path fanout tiebreaker"
./vliwScheduler simple.s submission/4_wide_critpath_fanout_source_simple.s 5
echo "- rename"
./vliwScheduler simple.s submission/4_wide_rename_source_simple.s 6
echo "done"

(cd submission && zip project1_code.zip *)
mv submission/project1_code.zip .
./project1_zip_validator.py