mkdir -p out;

./vliwScheduler in/add_resource_cap.s out/add_resource_cap.s 0;
./vliwScheduler in/mul_cap.s out/mul_cap.s 0;
./vliwScheduler in/stw_cap.s out/stw_cap.s 0;
./vliwScheduler in/ldw_cap.s out/ldw_cap.s 0;
./vliwScheduler in/mov_is_alu.s out/mov_is_alu.s 0;
./vliwScheduler in/all_instructions.s out/all_instructions.s 0;

./vliwScheduler in/branch_compare_hazards.s out/branch_compare_hazards.s 0;

./vliwScheduler in/critical_path.s out/critical_path.s 1;
./vliwScheduler in/resource.s out/resource.s 2;
./vliwScheduler in/fanout.s out/fanout.s 3;

./vliwScheduler in/ignores_transative_dependencies.s out/ignores_transative_dependencies.s 3;

./vliwScheduler in/fake_bank_dependencies.s out/fake_bank_dependencies.s 0;

./vliwScheduler in/crit_resource_tie.s out/crit_resource_tie.s 4;
./vliwScheduler in/crit_fanout_tie.s out/crit_fanout_tie.s 5;

./vliwScheduler in/mem_raw.s out/mem_raw.s 0;
./vliwScheduler in/mem_war.s out/mem_war.s 0;
./vliwScheduler in/mem_waw.s out/mem_waw.s 0;

./vliwScheduler in/branch_raw.s out/branch_raw.s 0;
./vliwScheduler in/branch_war.s out/branch_war.s 0;
./vliwScheduler in/branch_waw.s out/branch_waw.s 0;

./vliwScheduler in/raw.s out/raw.s 0;
./vliwScheduler in/war.s out/war.s 0;
./vliwScheduler in/waw.s out/waw.s 0;

./vliwScheduler in/mov_war.s out/mov_war.s 0;

for fn in `ls in`
do
    if cmp --silent expected/$fn out/$fn; then
        echo "- $fn Success"
    else
        diff expected/$fn out/$fn
        echo "- $fn FAILURE"
    fi
done
echo "DONE"
