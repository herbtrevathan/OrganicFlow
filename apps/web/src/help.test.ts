import {describe,it,expect} from 'vitest';
const help={workspace:'#docs-workspaces',workflow:'#docs-workflows',diff:'#docs-diffs'};
describe('help registry',()=>{it('has stable anchors',()=>{expect(Object.values(help).every(v=>v.startsWith('#docs-'))).toBe(true)});it('covers major surfaces',()=>expect(Object.keys(help)).toContain('workflow'))});
