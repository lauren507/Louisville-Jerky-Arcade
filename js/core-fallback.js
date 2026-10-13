// Minimal stand-ins for arcade-core.js so the page (filters, records, settings,
// Gift Quest, Prize Shelf) still runs when the game modules are not installed.
export const ACTION_KEYS={ArrowUp:'up',KeyW:'up',ArrowDown:'down',KeyS:'down',ArrowLeft:'left',KeyA:'left',ArrowRight:'right',KeyD:'right',KeyZ:'a',Space:'a',KeyX:'b'};
export class InputState{
  constructor(){this.sources=new Map();}
  set(source,action,down){if(down)this.sources.set(source,action);else this.sources.delete(source);}
  isDown(action){for(const a of this.sources.values())if(a===action)return true;return false;}
  snapshot(){const s={};for(const a of this.sources.values())s[a]=true;return s;}
  clear(){this.sources.clear();}
}
export class FixedClock{
  constructor(step=1/60){this.step=step;this.reset();}
  reset(){this.last=0;this.acc=0;}
  advance(now,fn){if(!this.last){this.last=now;return;}this.acc+=Math.min(.25,(now-this.last)/1000);this.last=now;while(this.acc>=this.step){fn(this.step);this.acc-=this.step;}}
}
export function cleanRecords(raw,ids){const out={};for(const id of ids){const r=raw?.[id];if(r&&Number.isFinite(r.score))out[id]={score:Math.max(0,Math.floor(r.score)),initials:String(r.initials||'YOU').slice(0,3),won:!!r.won};}return out;}
export function paddedScore(n){return String(Math.max(0,Math.floor(Number(n)||0))).padStart(6,'0').slice(-6);}
